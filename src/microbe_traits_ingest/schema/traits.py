# Auto generated from None by pythongen.py version: 0.0.1
# Generation date: 2024-07-05T15:48:45
# Schema: TraitsSchema
#
# id: https://w3id.org/traits
# description: A schema for representing traits of organisms.
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from datetime import date, datetime
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import String

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
TRAITS = CurieNamespace('traits', 'https://w3id.org/traits/')
DEFAULT_ = TRAITS


# Types

# Class references


@dataclass
class Traits(YAMLRoot):
    """
    A class representing various traits of an organism.
    """

    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TRAITS["Traits"]
    class_class_curie: ClassVar[str] = "traits:Traits"
    class_name: ClassVar[str] = "Traits"
    class_model_uri: ClassVar[URIRef] = TRAITS.Traits

    tax_id: str = None
    name: Optional[str] = None
    species_tax_id: Optional[str] = None
    data_source: Optional[str] = None
    org_name: Optional[str] = None
    species: Optional[str] = None
    genus: Optional[str] = None
    family: Optional[str] = None
    order: Optional[str] = None
    class_: Optional[str] = None
    phylum: Optional[str] = None
    superkingdom: Optional[str] = None
    gram_stain: Optional[str] = None
    metabolism: Optional[str] = None
    pathways: Optional[str] = None
    carbon_substrates: Optional[str] = None
    sporulation: Optional[str] = None
    motility: Optional[str] = None
    range_tmp: Optional[str] = None
    range_salinity: Optional[str] = None
    cell_shape: Optional[str] = None
    isolation_source: Optional[str] = None
    d1_lo: Optional[str] = None
    d1_up: Optional[str] = None
    d2_lo: Optional[str] = None
    d2_up: Optional[str] = None
    doubling_h: Optional[str] = None
    genome_size: Optional[str] = None
    gc_content: Optional[str] = None
    coding_genes: Optional[str] = None
    optimum_tmp: Optional[str] = None
    optimum_ph: Optional[str] = None
    growth_tmp: Optional[str] = None
    rRNA16S_genes: Optional[str] = None
    tRNA_genes: Optional[str] = None
    ref_id: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.tax_id):
            self.MissingRequiredField("tax_id")
        if not isinstance(self.tax_id, str):
            self.tax_id = str(self.tax_id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.species_tax_id is not None and not isinstance(self.species_tax_id, str):
            self.species_tax_id = str(self.species_tax_id)

        if self.data_source is not None and not isinstance(self.data_source, str):
            self.data_source = str(self.data_source)

        if self.org_name is not None and not isinstance(self.org_name, str):
            self.org_name = str(self.org_name)

        if self.species is not None and not isinstance(self.species, str):
            self.species = str(self.species)

        if self.genus is not None and not isinstance(self.genus, str):
            self.genus = str(self.genus)

        if self.family is not None and not isinstance(self.family, str):
            self.family = str(self.family)

        if self.order is not None and not isinstance(self.order, str):
            self.order = str(self.order)

        if self.class_ is not None and not isinstance(self.class_, str):
            self.class_ = str(self.class_)

        if self.phylum is not None and not isinstance(self.phylum, str):
            self.phylum = str(self.phylum)

        if self.superkingdom is not None and not isinstance(self.superkingdom, str):
            self.superkingdom = str(self.superkingdom)

        if self.gram_stain is not None and not isinstance(self.gram_stain, str):
            self.gram_stain = str(self.gram_stain)

        if self.metabolism is not None and not isinstance(self.metabolism, str):
            self.metabolism = str(self.metabolism)

        if self.pathways is not None and not isinstance(self.pathways, str):
            self.pathways = str(self.pathways)

        if self.carbon_substrates is not None and not isinstance(self.carbon_substrates, str):
            self.carbon_substrates = str(self.carbon_substrates)

        if self.sporulation is not None and not isinstance(self.sporulation, str):
            self.sporulation = str(self.sporulation)

        if self.motility is not None and not isinstance(self.motility, str):
            self.motility = str(self.motility)

        if self.range_tmp is not None and not isinstance(self.range_tmp, str):
            self.range_tmp = str(self.range_tmp)

        if self.range_salinity is not None and not isinstance(self.range_salinity, str):
            self.range_salinity = str(self.range_salinity)

        if self.cell_shape is not None and not isinstance(self.cell_shape, str):
            self.cell_shape = str(self.cell_shape)

        if self.isolation_source is not None and not isinstance(self.isolation_source, str):
            self.isolation_source = str(self.isolation_source)

        if self.d1_lo is not None and not isinstance(self.d1_lo, str):
            self.d1_lo = str(self.d1_lo)

        if self.d1_up is not None and not isinstance(self.d1_up, str):
            self.d1_up = str(self.d1_up)

        if self.d2_lo is not None and not isinstance(self.d2_lo, str):
            self.d2_lo = str(self.d2_lo)

        if self.d2_up is not None and not isinstance(self.d2_up, str):
            self.d2_up = str(self.d2_up)

        if self.doubling_h is not None and not isinstance(self.doubling_h, str):
            self.doubling_h = str(self.doubling_h)

        if self.genome_size is not None and not isinstance(self.genome_size, str):
            self.genome_size = str(self.genome_size)

        if self.gc_content is not None and not isinstance(self.gc_content, str):
            self.gc_content = str(self.gc_content)

        if self.coding_genes is not None and not isinstance(self.coding_genes, str):
            self.coding_genes = str(self.coding_genes)

        if self.optimum_tmp is not None and not isinstance(self.optimum_tmp, str):
            self.optimum_tmp = str(self.optimum_tmp)

        if self.optimum_ph is not None and not isinstance(self.optimum_ph, str):
            self.optimum_ph = str(self.optimum_ph)

        if self.growth_tmp is not None and not isinstance(self.growth_tmp, str):
            self.growth_tmp = str(self.growth_tmp)

        if self.rRNA16S_genes is not None and not isinstance(self.rRNA16S_genes, str):
            self.rRNA16S_genes = str(self.rRNA16S_genes)

        if self.tRNA_genes is not None and not isinstance(self.tRNA_genes, str):
            self.tRNA_genes = str(self.tRNA_genes)

        if self.ref_id is not None and not isinstance(self.ref_id, str):
            self.ref_id = str(self.ref_id)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass


slots.traits__name = Slot(
    uri=TRAITS.name,
    name="traits__name",
    curie=TRAITS.curie('name'),
    model_uri=TRAITS.traits__name,
    domain=None,
    range=Optional[str],
)

slots.traits__tax_id = Slot(
    uri=TRAITS.tax_id,
    name="traits__tax_id",
    curie=TRAITS.curie('tax_id'),
    model_uri=TRAITS.traits__tax_id,
    domain=None,
    range=str,
)

slots.traits__species_tax_id = Slot(
    uri=TRAITS.species_tax_id,
    name="traits__species_tax_id",
    curie=TRAITS.curie('species_tax_id'),
    model_uri=TRAITS.traits__species_tax_id,
    domain=None,
    range=Optional[str],
)

slots.traits__data_source = Slot(
    uri=TRAITS.data_source,
    name="traits__data_source",
    curie=TRAITS.curie('data_source'),
    model_uri=TRAITS.traits__data_source,
    domain=None,
    range=Optional[str],
)

slots.traits__org_name = Slot(
    uri=TRAITS.org_name,
    name="traits__org_name",
    curie=TRAITS.curie('org_name'),
    model_uri=TRAITS.traits__org_name,
    domain=None,
    range=Optional[str],
)

slots.traits__species = Slot(
    uri=TRAITS.species,
    name="traits__species",
    curie=TRAITS.curie('species'),
    model_uri=TRAITS.traits__species,
    domain=None,
    range=Optional[str],
)

slots.traits__genus = Slot(
    uri=TRAITS.genus,
    name="traits__genus",
    curie=TRAITS.curie('genus'),
    model_uri=TRAITS.traits__genus,
    domain=None,
    range=Optional[str],
)

slots.traits__family = Slot(
    uri=TRAITS.family,
    name="traits__family",
    curie=TRAITS.curie('family'),
    model_uri=TRAITS.traits__family,
    domain=None,
    range=Optional[str],
)

slots.traits__order = Slot(
    uri=TRAITS.order,
    name="traits__order",
    curie=TRAITS.curie('order'),
    model_uri=TRAITS.traits__order,
    domain=None,
    range=Optional[str],
)

slots.traits__class_ = Slot(
    uri=TRAITS.class_,
    name="traits__class_",
    curie=TRAITS.curie('class_'),
    model_uri=TRAITS.traits__class_,
    domain=None,
    range=Optional[str],
)

slots.traits__phylum = Slot(
    uri=TRAITS.phylum,
    name="traits__phylum",
    curie=TRAITS.curie('phylum'),
    model_uri=TRAITS.traits__phylum,
    domain=None,
    range=Optional[str],
)

slots.traits__superkingdom = Slot(
    uri=TRAITS.superkingdom,
    name="traits__superkingdom",
    curie=TRAITS.curie('superkingdom'),
    model_uri=TRAITS.traits__superkingdom,
    domain=None,
    range=Optional[str],
)

slots.traits__gram_stain = Slot(
    uri=TRAITS.gram_stain,
    name="traits__gram_stain",
    curie=TRAITS.curie('gram_stain'),
    model_uri=TRAITS.traits__gram_stain,
    domain=None,
    range=Optional[str],
)

slots.traits__metabolism = Slot(
    uri=TRAITS.metabolism,
    name="traits__metabolism",
    curie=TRAITS.curie('metabolism'),
    model_uri=TRAITS.traits__metabolism,
    domain=None,
    range=Optional[str],
)

slots.traits__pathways = Slot(
    uri=TRAITS.pathways,
    name="traits__pathways",
    curie=TRAITS.curie('pathways'),
    model_uri=TRAITS.traits__pathways,
    domain=None,
    range=Optional[str],
)

slots.traits__carbon_substrates = Slot(
    uri=TRAITS.carbon_substrates,
    name="traits__carbon_substrates",
    curie=TRAITS.curie('carbon_substrates'),
    model_uri=TRAITS.traits__carbon_substrates,
    domain=None,
    range=Optional[str],
)

slots.traits__sporulation = Slot(
    uri=TRAITS.sporulation,
    name="traits__sporulation",
    curie=TRAITS.curie('sporulation'),
    model_uri=TRAITS.traits__sporulation,
    domain=None,
    range=Optional[str],
)

slots.traits__motility = Slot(
    uri=TRAITS.motility,
    name="traits__motility",
    curie=TRAITS.curie('motility'),
    model_uri=TRAITS.traits__motility,
    domain=None,
    range=Optional[str],
)

slots.traits__range_tmp = Slot(
    uri=TRAITS.range_tmp,
    name="traits__range_tmp",
    curie=TRAITS.curie('range_tmp'),
    model_uri=TRAITS.traits__range_tmp,
    domain=None,
    range=Optional[str],
)

slots.traits__range_salinity = Slot(
    uri=TRAITS.range_salinity,
    name="traits__range_salinity",
    curie=TRAITS.curie('range_salinity'),
    model_uri=TRAITS.traits__range_salinity,
    domain=None,
    range=Optional[str],
)

slots.traits__cell_shape = Slot(
    uri=TRAITS.cell_shape,
    name="traits__cell_shape",
    curie=TRAITS.curie('cell_shape'),
    model_uri=TRAITS.traits__cell_shape,
    domain=None,
    range=Optional[str],
)

slots.traits__isolation_source = Slot(
    uri=TRAITS.isolation_source,
    name="traits__isolation_source",
    curie=TRAITS.curie('isolation_source'),
    model_uri=TRAITS.traits__isolation_source,
    domain=None,
    range=Optional[str],
)

slots.traits__d1_lo = Slot(
    uri=TRAITS.d1_lo,
    name="traits__d1_lo",
    curie=TRAITS.curie('d1_lo'),
    model_uri=TRAITS.traits__d1_lo,
    domain=None,
    range=Optional[str],
)

slots.traits__d1_up = Slot(
    uri=TRAITS.d1_up,
    name="traits__d1_up",
    curie=TRAITS.curie('d1_up'),
    model_uri=TRAITS.traits__d1_up,
    domain=None,
    range=Optional[str],
)

slots.traits__d2_lo = Slot(
    uri=TRAITS.d2_lo,
    name="traits__d2_lo",
    curie=TRAITS.curie('d2_lo'),
    model_uri=TRAITS.traits__d2_lo,
    domain=None,
    range=Optional[str],
)

slots.traits__d2_up = Slot(
    uri=TRAITS.d2_up,
    name="traits__d2_up",
    curie=TRAITS.curie('d2_up'),
    model_uri=TRAITS.traits__d2_up,
    domain=None,
    range=Optional[str],
)

slots.traits__doubling_h = Slot(
    uri=TRAITS.doubling_h,
    name="traits__doubling_h",
    curie=TRAITS.curie('doubling_h'),
    model_uri=TRAITS.traits__doubling_h,
    domain=None,
    range=Optional[str],
)

slots.traits__genome_size = Slot(
    uri=TRAITS.genome_size,
    name="traits__genome_size",
    curie=TRAITS.curie('genome_size'),
    model_uri=TRAITS.traits__genome_size,
    domain=None,
    range=Optional[str],
)

slots.traits__gc_content = Slot(
    uri=TRAITS.gc_content,
    name="traits__gc_content",
    curie=TRAITS.curie('gc_content'),
    model_uri=TRAITS.traits__gc_content,
    domain=None,
    range=Optional[str],
)

slots.traits__coding_genes = Slot(
    uri=TRAITS.coding_genes,
    name="traits__coding_genes",
    curie=TRAITS.curie('coding_genes'),
    model_uri=TRAITS.traits__coding_genes,
    domain=None,
    range=Optional[str],
)

slots.traits__optimum_tmp = Slot(
    uri=TRAITS.optimum_tmp,
    name="traits__optimum_tmp",
    curie=TRAITS.curie('optimum_tmp'),
    model_uri=TRAITS.traits__optimum_tmp,
    domain=None,
    range=Optional[str],
)

slots.traits__optimum_ph = Slot(
    uri=TRAITS.optimum_ph,
    name="traits__optimum_ph",
    curie=TRAITS.curie('optimum_ph'),
    model_uri=TRAITS.traits__optimum_ph,
    domain=None,
    range=Optional[str],
)

slots.traits__growth_tmp = Slot(
    uri=TRAITS.growth_tmp,
    name="traits__growth_tmp",
    curie=TRAITS.curie('growth_tmp'),
    model_uri=TRAITS.traits__growth_tmp,
    domain=None,
    range=Optional[str],
)

slots.traits__rRNA16S_genes = Slot(
    uri=TRAITS.rRNA16S_genes,
    name="traits__rRNA16S_genes",
    curie=TRAITS.curie('rRNA16S_genes'),
    model_uri=TRAITS.traits__rRNA16S_genes,
    domain=None,
    range=Optional[str],
)

slots.traits__tRNA_genes = Slot(
    uri=TRAITS.tRNA_genes,
    name="traits__tRNA_genes",
    curie=TRAITS.curie('tRNA_genes'),
    model_uri=TRAITS.traits__tRNA_genes,
    domain=None,
    range=Optional[str],
)

slots.traits__ref_id = Slot(
    uri=TRAITS.ref_id,
    name="traits__ref_id",
    curie=TRAITS.curie('ref_id'),
    model_uri=TRAITS.traits__ref_id,
    domain=None,
    range=Optional[str],
)
