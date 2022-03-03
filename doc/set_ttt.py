import re

keywords = ["ATTRIBUTE", "INSTANCE", "COLLECTION",
            "VODML", "MODEL", "REPORT", "TEMPLATES", "GLOBALS",
            "REFERENCE", "JOIN", "FOREIGN\\_KEY", "PRIMARY\\_KEY", "WHERE",
            "@name", "@uri",
            "@dmrole", "@dmtype",
            "@value", "@unit", "@arrayindex",
            "@tableref", "@ref",
            "@dmref", "@dmid", "@url", "@dmid", "@sourceref", "@primarykey", "@foreignkey"
            ]
# Output 'Jessa_knows_testing_and_machine_learning'

filename = "element_join.tex"
with open(filename) as fr:
    str = fr.read()
    for keyword in keywords:
        str = re.sub(r"[^\{:](" + keyword + ")[^\}]", ' BaSltexttt{\\1} ', str)
    
    print(str.replace('BaSl', '\\'))
    
