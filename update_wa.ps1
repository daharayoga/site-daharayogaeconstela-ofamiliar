$ErrorActionPreference = "Stop"

$filePath = ".\index.html"
$content = Get-Content -Raw -Path $filePath -Encoding UTF8

# WhatsApp regex
$content = $content -replace 'https://wa\.me/5519981381560[^"]*', 'https://wa.me/5519981381560?text=Ol%C3%A1%21+Vim+pelo+site+e+gostaria+de+saber+mais+sobre+os+atendimentos+da+Dahara+Yoga+e+Constela%C3%A7%C3%A3o+Familiar.'

Set-Content -Path $filePath -Value $content -Encoding UTF8
Write-Host "WhatsApp links updated in index.html"
