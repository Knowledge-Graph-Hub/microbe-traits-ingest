import uuid  # For generating UUIDs for associations

from biolink_model.datamodel.pydanticmodel_v2 import (
    Association,
    BiologicalProcess,
    OrganismTaxon,
)
from koza.cli_utils import get_koza_app
from oaklib.datamodels.text_annotator import TextAnnotationConfiguration
from tqdm import tqdm

from microbe_traits_ingest.constants import (
    CARBON_SUBSTRATES,
    CELL_SHAPE,
    CLASS_,
    CODING_GENES,
    D1_LO,
    D1_UP,
    D2_LO,
    D2_UP,
    DATA_SOURCE,
    DOUBLING_H,
    FAMILY,
    GC_CONTENT,
    GENOME_SIZE,
    GENUS,
    GRAM_STAIN,
    GROWTH_TMP,
    ISOLATION_SOURCE,
    METABOLISM,
    MOTILITY,
    NCBITAXON_PREFIX,
    OPTIMUM_PH,
    OPTIMUM_TMP,
    ORDER,
    ORG_NAME,
    PATHWAYS,
    PHYLUM,
    RANGE_SALINITY,
    RANGE_TMP,
    REF_ID,
    RRNA16S_GENES,
    SPECIES,
    SPECIES_TAX_ID,
    SPORULATION,
    SUPERKINGDOM,
    TAX_ID,
    TAXON_PATHWAY_PREDICATE,
    TRNA_GENES,
)
from microbe_traits_ingest.schema import Traits
from microbe_traits_ingest.schema.utils import get_oi

koza_app = get_koza_app("microbe-traits")

while (row := koza_app.get_row()) is not None:
    # Code to transform each row of data
    # For more information, see https://koza.monarchinitiative.org/Ingests/transform
    # entity_a = Entity(
    #     id=f"XMPL:00000{row['example_column_1'].split('_')[-1]}",
    #     name=row["example_column_1"],
    #     category=["biolink:Entity"],
    # )
    # entity_b = Entity(
    #     id=f"XMPL:00000{row['example_column_2'].split('_')[-1]}",
    #     name=row["example_column_2"],
    #     category=["biolink:Entity"],
    # )
    # association = Association(
    #     id=str(uuid.uuid1()),
    #     subject=row["example_column_1"],
    #     predicate=row["example_column_3"],
    #     object=row["example_column_2"],
    #     subject_category="SUBJ",
    #     object_category="OBJ",
    #     category=["biolink:Association"],
    #     knowledge_level="not_provided",
    #     agent_type="not_provided",
    # )
    # koza_app.write(entity_a, entity_b, association)
    # ********************************************************************************
    rows = iter(koza_app.get_row, None)
    upa_adapter = get_oi("upa")
    configuration = TextAnnotationConfiguration(
        include_aliases=True,
        matches_whole_text=True,
    )

    for row in tqdm(rows, desc="Processing rows", unit="row"):
        trait_object = Traits(
            tax_id=row[TAX_ID],
            name=row[ORG_NAME],
            species_tax_id=row[SPECIES_TAX_ID],
            data_source=row[DATA_SOURCE],
            org_name=row[ORG_NAME],
            species=row[SPECIES],
            genus=row[GENUS],
            family=row[FAMILY],
            order=row[ORDER],
            class_=row[CLASS_],  # 'class' is a reserved keyword in Python, so we use 'class_'
            phylum=row[PHYLUM],
            superkingdom=row[SUPERKINGDOM],
            gram_stain=row[GRAM_STAIN],
            metabolism=row[METABOLISM],
            pathways=row[PATHWAYS],
            carbon_substrates=row[CARBON_SUBSTRATES],
            sporulation=row[SPORULATION],
            motility=row[MOTILITY],
            range_tmp=row[RANGE_TMP],
            range_salinity=row[RANGE_SALINITY],
            cell_shape=row[CELL_SHAPE],
            isolation_source=row[ISOLATION_SOURCE],
            d1_lo=row[D1_LO],
            d1_up=row[D1_UP],
            d2_lo=row[D2_LO],
            d2_up=row[D2_UP],
            doubling_h=row[DOUBLING_H],
            genome_size=row[GENOME_SIZE],
            gc_content=row[GC_CONTENT],
            coding_genes=row[CODING_GENES],
            optimum_tmp=row[OPTIMUM_TMP],
            optimum_ph=row[OPTIMUM_PH],
            growth_tmp=row[GROWTH_TMP],
            rRNA16S_genes=row[RRNA16S_GENES],
            tRNA_genes=row[TRNA_GENES],
            ref_id=row[REF_ID],
        )
        organism = OrganismTaxon(
            id=f"{NCBITAXON_PREFIX}:{trait_object.tax_id}",
            name=trait_object.org_name,
        )
        if trait_object.pathways:
            try:
                annotations = upa_adapter.annotate_text(trait_object.pathways, configuration)
            except Exception as e:
                print(f"Error annotating text: {e}")
                continue
            for annotation in annotations:
                if annotation.object_id:
                    pathway = BiologicalProcess(
                        id=annotation.object_id,
                        name=annotation.object_label,
                    )
                    association = Association(
                        id=str(uuid.uuid1()),
                        subject=organism.id,
                        predicate=TAXON_PATHWAY_PREDICATE,
                        object=pathway.id,
                        subject_category=organism.category[0],
                        object_category=pathway.category[0],
                        knowledge_level="not_provided",
                        agent_type="not_provided",
                    )
                    koza_app.output_dir = koza_app.output_dir / "pathways"
                    koza_app.write(organism, pathway, association)
