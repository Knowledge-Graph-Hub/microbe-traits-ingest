import json
import uuid  # For generating UUIDs for associations
from collections import defaultdict
from os import makedirs
from pathlib import Path

from biolink_model.datamodel.pydanticmodel_v2 import (
    Association,
    BiologicalProcess,
    ChemicalEntity,
    ChemicalRole,
    OrganismTaxon,
)
from koza.cli_utils import get_koza_app
from oaklib.datamodels.text_annotator import TextAnnotation, TextAnnotationConfiguration
from tqdm import tqdm

from microbe_traits_ingest.constants import (
    ANNOTATION_KEY,
    CARBON_SUBSTRATE_PREFIX,
    CARBON_SUBSTRATE_ROLE_PREDICATE,
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
    HAS_ROLE,
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
    ROLES_KEY,
    RRNA16S_GENES,
    SPECIES,
    SPECIES_TAX_ID,
    SPORULATION,
    SUPERKINGDOM,
    TAX_ID,
    TAXON_CARBON_SUBSTRATE_PREDICATE,
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
pathways_annotations_map = defaultdict(dict)
pathways_set = set()
pathways_annotated = False
carbon_substrates_annotations_and_roles_map = defaultdict(dict)
carbon_substrates_set = set()
carbon_substrates_set_not_annotated = set()
carbon_substrates_annotated = False
makedirs(TMP_DIR, exist_ok=True)

# Load existing pathways annotations if available
if pathways_annotation_file_path.exists():
    with open(pathways_annotation_file_path, "r") as f:
        next(f)  # Skip header
        pathways_annotations_map = {
            line.split("\t")[0]: TextAnnotation(object_id=line.split("\t")[1], object_label=line.split("\t")[2])
            for line in f.readlines()
        }
        pathways_set.update(annotation for annotation in pathways_annotations_map.keys())
        pathways_annotated = True
if carbon_substrates_annotation_file_path.exists():
    with open(carbon_substrates_annotation_file_path, "r") as f:
        try:
            carbon_substrates_annotations_and_roles_map = {
                k: v for line in f if line.strip() for k, v in json.loads(line).items()
            }
        except json.JSONDecodeError:
            carbon_substrates_annotations_and_roles_map = {}
        carbon_substrates_set.update(substrate for substrate in carbon_substrates_annotations_and_roles_map.keys())
        carbon_substrates_annotated = True


total_rows = 172324  #! Total number of rows in the dataset: manually entered.

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
                        if trait_object.pathways not in pathways_set:
                            f.write(f"{trait_object.pathways}\t{annotation.object_id}\t{annotation.object_label}\n")
                            pathways_annotations_map[trait_object.pathways] = annotation
                            pathways_set.add(trait_object.pathways)

            if trait_object.pathways in pathways_annotations_map:
                annotation = pathways_annotations_map[trait_object.pathways]
                pathway = BiologicalProcess(
                    id=annotation.object_id,
                    name=annotation.object_label,
                )
            else:
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

        # Open the file in append mode for streaming
        with open(carbon_substrates_annotation_file_path, 'a') as json_file:
            # Handle carbon substrates annotations
            if trait_object.carbon_substrates and trait_object.carbon_substrates != "NA":
                split_substrates = trait_object.carbon_substrates.split(", ")
                for substrate in split_substrates:
                    if not carbon_substrates_annotated:
                        annotations = chebi_adapter.annotate_text(substrate, configuration)
                        if (
                            substrate not in carbon_substrates_set
                            and substrate not in carbon_substrates_set_not_annotated
                        ):
                            # Update the set if the substrate is not in any of the object_labels in the annotations list
                            if all(substrate != annotation.object_label for annotation in annotations):
                                carbon_substrates_set_not_annotated.add(substrate)
                            else:
                                for annotation in annotations:
                                    if substrate not in carbon_substrates_set:
                                        if annotation.object_label.lower() == substrate.lower():
                                            roles_object_list = []
                                            substrate_roles = set(
                                                chebi_adapter.relationships(
                                                    subjects={annotation.object_id}, predicates=[HAS_ROLE]
                                                )
                                            )
                                            if substrate_roles != set():
                                                for role in substrate_roles:
                                                    chemical_role = ChemicalRole(
                                                        id=role[2],
                                                        name=chebi_adapter.label(role[2]),
                                                        has_attribute_type="role",
                                                    )
                                                    roles_object_list.append(chemical_role)

                                            # Update the map
                                            carbon_substrates_annotations_and_roles_map[substrate] = {
                                                ANNOTATION_KEY: {
                                                    "object_id": annotation.object_id,
                                                    "object_label": annotation.object_label,
                                                },
                                                ROLES_KEY: [
                                                    {
                                                        "id": role.id,
                                                        "name": role.name,
                                                        "has_attribute_type": role.has_attribute_type,
                                                    }
                                                    for role in roles_object_list
                                                ],
                                            }

                                            # Add to the set
                                            carbon_substrates_set.add(substrate)

                                            # Write to the file
                                            json.dump(
                                                {substrate: carbon_substrates_annotations_and_roles_map[substrate]},
                                                json_file,
                                            )
                                            json_file.write("\n")

                    if substrate in carbon_substrates_annotations_and_roles_map:
                        annotation_data = carbon_substrates_annotations_and_roles_map[substrate][ANNOTATION_KEY]
                        roles_data = carbon_substrates_annotations_and_roles_map[substrate][ROLES_KEY]
                        carbon_substrate = ChemicalEntity(
                            id=annotation_data["object_id"],
                            name=annotation_data["object_label"],
                        )

                        carbon_substrate_roles = [
                            ChemicalRole(
                                id=role["id"], name=role["name"], has_attribute_type=role["has_attribute_type"]
                            )
                            for role in roles_data
                        ]
                    else:
                        carbon_substrate = ChemicalEntity(
                            id=f"{CARBON_SUBSTRATE_PREFIX}:{substrate.replace(' ', '_')}",
                            name=substrate,
                        )
                        carbon_substrate_roles = []

                    tax_carbon_substrate_association = Association(
                        id=str(uuid.uuid1()),
                        subject=carbon_substrate.id,
                        predicate=TAXON_CARBON_SUBSTRATE_PREDICATE,
                        object=organism.id,
                        subject_category=carbon_substrate.category[0],
                        object_category=organism.category[0],
                        knowledge_level="not_provided",
                        agent_type="not_provided",
                    )

                    koza_app.write(organism, carbon_substrate, tax_carbon_substrate_association)
                    if carbon_substrate_roles:
                        for role in carbon_substrate_roles:
                            role_association = Association(
                                id=str(uuid.uuid1()),
                                subject=carbon_substrate.id,
                                predicate=CARBON_SUBSTRATE_ROLE_PREDICATE,
                                object=role.id,
                                subject_category=carbon_substrate.category[0],
                                object_category=role.category[0],
                                knowledge_level="not_provided",
                                agent_type="not_provided",
                            )
                            koza_app.write(carbon_substrate, role, role_association)

        pbar.update(1)
