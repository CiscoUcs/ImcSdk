"""This module contains the general information for BiosVfPchUsb30Mode ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfPchUsb30ModeConsts:
    VP_PCH_USB30_MODE_DISABLED = "Disabled"
    VP_PCH_USB30_MODE_ENABLED = "Enabled"
    _VP_PCH_USB30_MODE_DISABLED = "disabled"
    _VP_PCH_USB30_MODE_ENABLED = "enabled"
    VP_PCH_USB30_MODE_PLATFORM_DEFAULT = "platform-default"


class BiosVfPchUsb30Mode(ManagedObject):
    """This is BiosVfPchUsb30Mode class."""

    consts = BiosVfPchUsb30ModeConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfPchUsb30Mode", "biosVfPchUsb30Mode", "PchUsb30-Mode", VersionMeta.Version202c, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], ["Get", "Set"]),
        "modular": MoMeta("BiosVfPchUsb30Mode", "biosVfPchUsb30Mode", "PchUsb30-Mode", VersionMeta.Version2013e, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version202c, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version202c, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version202c, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_pch_usb30_mode": MoPropertyMeta("vp_pch_usb30_mode", "vpPchUsb30Mode", "string", VersionMeta.Version202c, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version202c, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_pch_usb30_mode": MoPropertyMeta("vp_pch_usb30_mode", "vpPchUsb30Mode", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpPchUsb30Mode": "vp_pch_usb30_mode", 
            "childAction": "child_action", 
        },

        "modular": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpPchUsb30Mode": "vp_pch_usb30_mode", 
            "childAction": "child_action", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.status = None
        self.vp_pch_usb30_mode = None
        self.child_action = None

        ManagedObject.__init__(self, "BiosVfPchUsb30Mode", parent_mo_or_dn, **kwargs)

