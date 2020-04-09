"""This module contains the general information for BiosVfPatrolScrubDuration ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfPatrolScrubDurationConsts:
    VP_PATROL_SCRUB_DURATION_PLATFORM_DEFAULT = "platform-default"


class BiosVfPatrolScrubDuration(ManagedObject):
    """This is BiosVfPatrolScrubDuration class."""

    consts = BiosVfPatrolScrubDurationConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfPatrolScrubDuration", "biosVfPatrolScrubDuration", "Patrol-Scrub-Duration", VersionMeta.Version151f, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], ["Get", "Set"]),
        "modular": MoMeta("BiosVfPatrolScrubDuration", "biosVfPatrolScrubDuration", "Patrol-Scrub-Duration", VersionMeta.Version2013e, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
            "vp_patrol_scrub_duration": MoPropertyMeta("vp_patrol_scrub_duration", "vpPatrolScrubDuration", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["platform-default"], ["5-23"]), 
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
        },

        "modular": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
            "vp_patrol_scrub_duration": MoPropertyMeta("vp_patrol_scrub_duration", "vpPatrolScrubDuration", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["platform-default"], ["5-23"]), 
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpPatrolScrubDuration": "vp_patrol_scrub_duration", 
            "childAction": "child_action", 
        },

        "modular": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpPatrolScrubDuration": "vp_patrol_scrub_duration", 
            "childAction": "child_action", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.status = None
        self.vp_patrol_scrub_duration = None
        self.child_action = None

        ManagedObject.__init__(self, "BiosVfPatrolScrubDuration", parent_mo_or_dn, **kwargs)

