import uuid  # For generating UUIDs for associations
from pathlib import Path

from biolink_model.datamodel.pydanticmodel_v2 import (
    Association,
    BiologicalProcess,
    OrganismTaxon,
)
from koza.cli_utils import get_koza_app
from oaklib.datamodels.text_annotator import TextAnnotationConfiguration, TextAnnotation
from tqdm import tqdm
from os import makedirs

from microbe_traits_ingest.constants import (
    CARBON_SUBSTRATES,
    CARBON_SUBSTRATES_ANNOTATIONS_FILE,
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
    PATHWAY_ANNOTATIONS_FILE,
    PATHWAY_PREFIX,
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
    TMP_DIR,
    TRNA_GENES,
)
from microbe_traits_ingest.schema.traits_datamodel import Traits
from microbe_traits_ingest.utils import get_oi

koza_app = get_koza_app("microbe-traits")

# # Initialize the iterator
# rows = list(iter(koza_app.get_row, None))  # Convert to list to avoid exhaustion issues
# if not rows:
#     print("No rows to process.")
# else:
#     print(f"Total rows to process: {len(rows)}")

upa_adapter = get_oi("upa")
chebi_adapter = get_oi("chebi")
configuration = TextAnnotationConfiguration(
    include_aliases=True,
    matches_whole_text=True,
)

pathways_annotation_file_path = Path(f"{TMP_DIR}/{PATHWAY_ANNOTATIONS_FILE}")
carbon_substrates_annotation_file_path = Path(f"{TMP_DIR}/{CARBON_SUBSTRATES_ANNOTATIONS_FILE}")

# Initialize annotation maps and flags
pathways_annotations_map = {}
pathways_set = set()
pathways_annotated = False

# Load existing pathways annotations if available
if pathways_annotation_file_path.exists():
    with open(pathways_annotation_file_path, "r") as f:
        next(f)  # Skip header
        pathways_annotations_map = {
            line.split("\t")[0]: TextAnnotation(object_id=line.split("\t")[1], object_label=line.split("\t")[2])
            for line in f.readlines()
        }
        pathways_set.update(annotation.object_id for annotation in pathways_annotations_map.values())
        pathways_annotated = True
else:
    makedirs(TMP_DIR, exist_ok=True)

total_rows = 172324

with tqdm(total=total_rows, desc="Processing rows", unit="row") as pbar:
    while (row := koza_app.get_row()) is not None:
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

        # Handle pathways annotations
        if trait_object.pathways and trait_object.pathways != "NA":
            if not pathways_annotated:
                annotations = upa_adapter.annotate_text(trait_object.pathways, configuration)
                with open(pathways_annotation_file_path, "a") as f:
                    for annotation in annotations:
                        if annotation.object_id not in pathways_set:
                            f.write(f"{trait_object.pathways}\t{annotation.object_id}\t{annotation.object_label}\n")
                            pathways_annotations_map[trait_object.pathways] = annotation
                            pathways_set.add(annotation.object_id)


            if trait_object.pathways in pathways_annotations_map:
                annotation = pathways_annotations_map[trait_object.pathways]
                pathway = BiologicalProcess(
                    id=annotation.object_id,
                    name=annotation.object_label,
                )
            else:
                # print(f"Pathway not annotated: {trait_object.pathways}")
                pathway = BiologicalProcess(
                    id=f"{PATHWAY_PREFIX}:{trait_object.pathways}",
                    name=trait_object.pathways,
                )
            tax_path_association = Association(
                id=str(uuid.uuid1()),
                subject=organism.id,
                predicate=TAXON_PATHWAY_PREDICATE,
                object=pathway.id,
                subject_category=organism.category[0],
                object_category=pathway.category[0],
                knowledge_level="not_provided",
                agent_type="not_provided",
            )
                
            koza_app.write(organism, pathway, tax_path_association)

        pbar.update(1)
