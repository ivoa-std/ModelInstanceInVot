import re
import os
import shutil

keywords = ["ATTRIBUTE", "INSTANCE", "COLLECTION",
            "VODML", "MODEL", "REPORT", "TEMPLATES", "GLOBALS",
            "REFERENCE", "JOIN", "FOREIGN\\\\_KEY", "PRIMARY\\\\_KEY", "WHERE",
            "@name", "@uri",
            "@dmrole", "@dmtype",
            "@value", "@unit", "@arrayindex",
            "@tableref", "@ref",
            "@dmref", "@dmid", "@url", "@dmid", "@sourceref", "@primarykey", "@foreignkey"
            ]

dirs = os.listdir( "." )
for filename in dirs:
    if os.path.isfile(filename)  and filename.endswith(".tex") is True: 
        print(f"process {filename}")
        filename_org = filename + ".org"
        if os.path.exists(filename_org) is False:
            shutil.copyfile(filename, filename_org
                        )
        with open(filename_org) as fr:
            str = fr.read()            
            str = re.sub(r"([a-z] )dm", '\\1 @dm', str)

            for keyword in keywords:
                str = re.sub(r"[^\{:](" + keyword + ")[^\}]", ' BaSltexttt{\\1} ', str)
        
        with   open(filename, 'w') as fw:  
            fw.write(str.replace('BaSl', '\\').replace(' )', ')'))
    
"""
To fix by hand

in table missing & or \\
 e.g. \texttt{@value}  &

"""