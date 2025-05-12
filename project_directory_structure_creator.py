import os

# Define the full directory structure
directory_structure = [
    "weldmastergwinnett.com/README.md",
    "weldmastergwinnett.com/public/index.php",
    "weldmastergwinnett.com/public/phpinfo.php",
    "weldmastergwinnett.com/public/Assets/",
    "weldmastergwinnett.com/public/CSS/Base/A_body.css",
    "weldmastergwinnett.com/public/CSS/Base/B_header.css",
    "weldmastergwinnett.com/public/CSS/Base/C_nav.css",
    "weldmastergwinnett.com/public/CSS/Base/D_main.css",
    "weldmastergwinnett.com/public/CSS/Base/E_footer.css",
    "weldmastergwinnett.com/public/CSS/Components/card.css",
    "weldmastergwinnett.com/public/CSS/Components/home.css",
    "weldmastergwinnett.com/public/CSS/Components/leaderboard.css",
    "weldmastergwinnett.com/public/CSS/Components/table.css",
    "weldmastergwinnett.com/public/JS/Model/Cell.js",
    "weldmastergwinnett.com/public/JS/Model/Data.js",
    "weldmastergwinnett.com/public/JS/Model/Table.js",
    "weldmastergwinnett.com/public/JS/Utilities/handleCellClick.js",
    "weldmastergwinnett.com/public/JS/Utilities/hideLeaderboard.js",
    "weldmastergwinnett.com/public/JS/Utilities/insertData.js",
    "weldmastergwinnett.com/public/JS/Utilities/showSection.js",
    "weldmastergwinnett.com/public/JS/Utilities/toggleMenu.js",
    "weldmastergwinnett.com/app/create/process.php",
    "weldmastergwinnett.com/app/create/joint.php",
    "weldmastergwinnett.com/app/create/material.php",
    "weldmastergwinnett.com/app/create/thickness.php",
    "weldmastergwinnett.com/app/create/welder.php",
    "weldmastergwinnett.com/app/create/sample.php",
    "weldmastergwinnett.com/app/read/processes.php",
    "weldmastergwinnett.com/app/read/joints.php",
    "weldmastergwinnett.com/app/read/materials.php",
    "weldmastergwinnett.com/app/read/thicknesses.php",
    "weldmastergwinnett.com/app/read/welders.php",
    "weldmastergwinnett.com/app/read/samples.php",
    "weldmastergwinnett.com/app/update/process.php",
    "weldmastergwinnett.com/app/update/joint.php",
    "weldmastergwinnett.com/app/update/material.php",
    "weldmastergwinnett.com/app/update/thickness.php",
    "weldmastergwinnett.com/app/update/welder.php",
    "weldmastergwinnett.com/app/update/sample.php",
    "weldmastergwinnett.com/app/delete/process.php",
    "weldmastergwinnett.com/app/delete/joint.php",
    "weldmastergwinnett.com/app/delete/material.php",
    "weldmastergwinnett.com/app/delete/thickness.php",
    "weldmastergwinnett.com/app/delete/welder.php",
    "weldmastergwinnett.com/app/delete/sample.php",
    "weldmastergwinnett.com/app/views/home.view.php",
    "weldmastergwinnett.com/app/views/form.view.php",
    "weldmastergwinnett.com/app/views/table.view.php",
    "weldmastergwinnett.com/app/views/layout.view.php",
    "weldmastergwinnett.com/config/db.php",
    "weldmastergwinnett.com/SQL/schema.sql",
    "weldmastergwinnett.com/uploads/"
]

# Create all directories and empty files
for path in directory_structure:
    if path.endswith("/"):
        os.makedirs(path, exist_ok=True)
    else:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w") as f:
            pass  # create empty file

"Directory structure created successfully."
