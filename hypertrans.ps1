# Windows Powershell Script
# > ...hypertrans.ps1

# virtualenv activate
. $PSScriptRoot\_hypertrans\Scripts\activate.ps1

# module loop
python $PSScriptRoot\google_trans

# virtualenv deactivate
deactivate
