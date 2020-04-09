"""This module contains the general information for BiosVfCbsCmnGnbNbIOMMU ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfCbsCmnGnbNbIOMMUConsts:
    VP_CBS_CMN_GNB_NB_IOMMU_AUTO = "Auto"
    VP_CBS_CMN_GNB_NB_IOMMU_DISABLED = "Disabled"
    VP_CBS_CMN_GNB_NB_IOMMU_ENABLED = "Enabled"
    _VP_CBS_CMN_GNB_NB_IOMMU_DISABLED = "disabled"
    _VP_CBS_CMN_GNB_NB_IOMMU_ENABLED = "enabled"
    VP_CBS_CMN_GNB_NB_IOMMU_PLATFORM_DEFAULT = "platform-default"


class BiosVfCbsCmnGnbNbIOMMU(ManagedObject):
    """This is BiosVfCbsCmnGnbNbIOMMU class."""

    consts = BiosVfCbsCmnGnbNbIOMMUConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfCbsCmnGnbNbIOMMU", "biosVfCbsCmnGnbNbIOMMU", "io-mmu", VersionMeta.Version401a, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version401a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
            "vp_cbs_cmn_gnb_nb_iommu": MoPropertyMeta("vp_cbs_cmn_gnb_nb_iommu", "vpCbsCmnGnbNbIOMMU", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Auto", "Disabled", "Enabled", "disabled", "enabled", "platform-default"], []), 
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpCbsCmnGnbNbIOMMU": "vp_cbs_cmn_gnb_nb_iommu", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_cbs_cmn_gnb_nb_iommu = None

        ManagedObject.__init__(self, "BiosVfCbsCmnGnbNbIOMMU", parent_mo_or_dn, **kwargs)

