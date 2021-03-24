def NEO4J_SIMPLE_EVENT(event):
    return "(:Experiential{event:" + "\"{}\"".format(event) + "})-[:DURING]->(temporal:Temporal)-[:IS_PART_OF]->(video:Video)"

def NEO4J_SIMPLE_INFORMATION(information):
    return "(:Infromational{information:" + "\"{}\"".format(information) + "})-[:PRESENT]->(temporal:Temporal)-[:IS_PART_OF]->(video:Video)"

def NEO4J_SIMPLE_SPATIAL(spatial):
    return "(:Spatial{place:" + "\"{}\"".format(spatial) + "})-[:AT]->(temporal:Temporal)-[:IS_PART_OF]->(video:Video)"

def NEO4J_INFORMATION_INDEX(informationQuery,indexNum):
    return "CALL db.index.fulltext.queryNodes('informationalIndex'," + "\"{}\"".format(informationQuery) + ") YIELD node as info, score as s"+str(indexNum)

def NEO4J_EXPERIENTIAL_INDEX(informationQuery,indexNum):
    return "CALL db.index.fulltext.queryNodes('ExperentialIndex'," + "\"{}\"".format(informationQuery) + ") YIELD node as event, score as s"+str(indexNum)

def NEO4J_SPATIAL_INDEX(informationQuery,indexNum):
    return "CALL db.index.fulltext.queryNodes('spatialIndex'," + "\"{}\"".format(informationQuery) + ") YIELD node as spatial, score as s"+str(indexNum)

def NEO4J_FUZZY_SCORE_AGGR(numIndexes):
    res = ""
    for i in range(numIndexes):
        res += "s" + str(i) + "+"
    return res[:-1] + " as score"

INSERT = "INSERT"
SELECT = "SELECT"
MATCH = "MATCH "
UNION_MATCH = "UNION MATCH "

SPACE = " "
COMMA = ","

EXPERENTIAL = "EXPERENTIAL"
SPATIAL = "SPATIAL"
TEMPORAL = "TEMPORAL"
CAUSALITY = "CAUSALITY"
INFORMATIONAL = "INFORMATIONAL"
DATABASE = "DATABASE"
VIDEO = "VIDEO"

START_FRAME = "start_frame"
END_FRAME = "end_frame"

PARSED_DICT = "parsedDict"

WHERE = "WHERE"
AND = "AND"

NEO4J_NODE_MAPPING = {
    "event": EXPERENTIAL,
    "spatial": SPATIAL,
    "temporal" : TEMPORAL,
    "causality": CAUSALITY,
    "informational": INFORMATIONAL
}

NEO4J_NODE_NAMES = {
	EXPERENTIAL: "event",
	SPATIAL: "spatial",
	TEMPORAL: "temporal",
	CAUSALITY: "cause",
	INFORMATIONAL: "info",
	VIDEO: "video"
}

NEO4J_NODE_TYPE_MAPPING = {
    EXPERENTIAL: "(event:Experiential)",
    SPATIAL: "(spatial:Spatial)",
    TEMPORAL : "(temporal:Temporal)",
    CAUSALITY: "(cause:Causality)",
    INFORMATIONAL: "(info:Infromational)",
    VIDEO: "(video:Video)"
}

NEO4J_FUZZY_INDEX = {
    EXPERENTIAL: NEO4J_EXPERIENTIAL_INDEX,
    SPATIAL: NEO4J_SPATIAL_INDEX,
    INFORMATIONAL: NEO4J_INFORMATION_INDEX
}

NEO4J_FILTERS = {
    EXPERENTIAL: NEO4J_SIMPLE_EVENT,
    SPATIAL: NEO4J_SIMPLE_SPATIAL,
    INFORMATIONAL: NEO4J_SIMPLE_INFORMATION
}

NEO4J_RELATIONSHIP_VT = "IS_PART_OF"

NEO4J_RELATIONSHIP_IT = "PRESENT"

NEO4J_RELATIONSHIP_ET = "DURING"

NEO4J_RELATIONSHIP_ST = "AT"

NEO4J_SELECT_RETURN = " RETURN temporal,video"

NEO4J_RELATIONSHIPS = {
    EXPERENTIAL: "(event)-[:DURING]->(temporal:Temporal)",
    INFORMATIONAL: "(info)-[:PRESENT]->(temporal:Temporal)",
    SPATIAL: "(spatial)-[:AT]->(temporal:Temporal)",
    TEMPORAL: "(temporal)-[:IS_PART_OF]->(video:Video)"
}


YOUTUBE_DATA_API_BASE_PATH = "https://www.googleapis.com/youtube/v3/videos?id={}&key={}&part=contentDetails"