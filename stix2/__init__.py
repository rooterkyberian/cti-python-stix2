"""Python APIs for STIX 2."""

# flake8: noqa

import json

from .bundle import Bundle
from .common import ExternalReference, KillChainPhase
from .sdo import AttackPattern, Campaign, CourseOfAction, Identity, Indicator, \
    IntrusionSet, Malware, ObservedData, Report, ThreatActor, Tool, \
    Vulnerability
from .sro import Relationship, Sighting
from .markings import MarkingDefinition, GranularMarking, StatementMarking, TLPMarking


def parse(data):
    """Deserialize a string or file-like object into a STIX object"""

    if type(data) is dict:
        obj = data
    else:
        try:
            obj = json.loads(data)
        except TypeError:
            obj = json.load(data)

    obj_map = {
        'attack-pattern': AttackPattern,
        'campaign': Campaign,
        'course-of-action': CourseOfAction,
        'identity': Identity,
        'indicator': Indicator,
        'intrusion-set': IntrusionSet,
        'malware': Malware,
        'marking-definition': MarkingDefinition,
        'observed-data': ObservedData,
        'report': Report,
        'relationship': Relationship,
        'threat-actor': ThreatActor,
        'tool': Tool,
        'sighting': Sighting,
        'vulnerability': Vulnerability,
    }

    if 'type' not in obj:
        # TODO parse external references, kill chain phases, and granular markings
        pass
    else:
        try:
            obj_class = obj_map[obj['type']]
            return obj_class(**obj)
        except KeyError:
            # TODO handle custom objects
            raise ValueError("Can't parse unknown object type!")

    return obj
