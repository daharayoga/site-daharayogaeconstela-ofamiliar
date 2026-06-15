$ErrorActionPreference = "Stop"

$filePath = ".\index.html"
$content = Get-Content -Raw -Path $filePath -Encoding UTF8

# 1. Header mobile text
$content = $content -replace '(?i)(<img src="assets/img/logo-principal\.png" alt="Dahara Yoga e Constelação Familiar" class=")h-16 w-auto object-contain(" width="180" height="49">\s*</a>)', '$1h-14 sm:h-16 w-auto object-contain shrink-0$2`n        <span class="font-title font-semibold text-titleMain text-xs sm:text-sm leading-tight lg:hidden block ml-2">`n          Dahara Yoga e <br class="hidden sm:block">Constelação Familiar`n        </span>`n      </a>'

# 2. Testimonials wrap in <a> and 3. Remove initials
$content = $content -replace '(?s)<!-- Card Depoimento (\d+) -->\s*<div class="bg-white p-8 rounded-2xl border border-lineColor/50 shadow-sm flex flex-col justify-between">', '<!-- Card Depoimento $1 -->`n          <!-- Inserir link da avaliação do Google Maps no href="#" abaixo -->`n          <a href="#" target="_blank" rel="noopener" class="block bg-white p-8 rounded-2xl border border-lineColor/50 shadow-sm flex flex-col justify-between hover:shadow-md transition-shadow group">'

$content = $content -replace '(?s)<div class="border-t border-lineColor/50 pt-4 flex items-center gap-3">\s*<div class="w-10 h-10 rounded-full bg-accent1/30 flex items-center justify-center font-bold text-primary font-title">[A-Z]</div>\s*<div>\s*<h4 class="font-semibold text-sm text-titleMain">([^<]+)</h4>\s*</div>\s*</div>\s*</div>', '<div class="border-t border-lineColor/50 pt-4 flex items-center gap-3">`n              <!-- <img src="assets/img/placeholder.jpg" alt="$1" class="w-10 h-10 rounded-full object-cover"> -->`n              <div>`n                <h4 class="font-semibold text-sm text-titleMain group-hover:text-primary transition-colors">$1</h4>`n              </div>`n            </div>`n          </a>'

# 4. WhatsApp
$content = $content -replace 'href="https://wa\.me/5519981381560[^"]*"', 'href="https://wa.me/5519981381560?text=Ol%C3%A1%21+Vim+pelo+site+e+gostaria+de+saber+mais+sobre+os+atendimentos+da+Dahara+Yoga+e+Constela%C3%A7%C3%A3o+Familiar."'

# 6. Footer
$content = $content -replace '(<p>&copy; 202[45] Dahara Yoga e Constelação Familiar\. Todos os direitos reservados\.</p>)', '$1`n        <p class="text-xs mt-2 md:mt-0 text-textMain/60">`n          Projeto desenvolvido em parceria entre <a href="#" target="_blank" rel="noopener" class="hover:text-primary transition-colors">AXTRA</a> e <a href="#" target="_blank" rel="noopener" class="hover:text-primary transition-colors">Growmni</a>.`n        </p>'

Set-Content -Path $filePath -Value $content -Encoding UTF8
Write-Host "Processed index.html"

$buildPath = ".\build\index.html"
if (Test-Path $buildPath) {
    Set-Content -Path $buildPath -Value $content -Encoding UTF8
    Write-Host "Processed build/index.html"
}
