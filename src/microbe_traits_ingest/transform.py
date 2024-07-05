import uuid  # For generating UUIDs for associations

from biolink_model.datamodel.pydanticmodel_v2 import (
    OrganismTaxon,
    Association,
    ChemicalEntity,
    ChemicalRole,
    BiologicalProcess,
    ActivityAndBehavior,
)
from koza.cli_utils import get_koza_app

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
    print(row)
    import pdb; pdb.set_trace()
