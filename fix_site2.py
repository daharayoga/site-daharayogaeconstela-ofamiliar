import re
import os

def process_html(filepath):
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Mobile Header text
    # Original:
    # <img src="assets/img/logo-principal.png" alt="Dahara Yoga e Constelação Familiar" class="h-16 w-auto object-contain" width="180" height="49">
    # </a>
    logo_regex = re.compile(r'(<img src="assets/img/logo-principal\.png" alt="Dahara Yoga e Constelação Familiar" class="h-16 w-auto object-contain"[^>]*>)\s*</a>', re.IGNORECASE)
    if logo_regex.search(content):
        # We replace the h-16 with a responsive size so it fits, and add the text.
        replacement = r'''\1
        <span class="font-title font-semibold text-titleMain text-xs sm:text-sm leading-tight lg:hidden block ml-2">
          Dahara Yoga e <br class="hidden sm:block">Constelação Familiar
        </span>
      </a>'''
        # Also need to make the container flex and adjust gap if needed. The <a> already has 'flex items-center gap-3'.
        # Wait, the img has class="h-16 w-auto object-contain". Let's change it to h-14 sm:h-16 to fit better on mobile.
        def logo_repl(match):
            img_tag = match.group(1)
            img_tag = img_tag.replace('h-16', 'h-14 sm:h-16 shrink-0')
            return img_tag + '''
        <span class="font-title font-semibold text-titleMain text-sm leading-tight lg:hidden block">
          Dahara Yoga e<br>Constelação Familiar
        </span>
      </a>'''
        content = logo_regex.sub(logo_repl, content)

    # 2 & 3. Testimonials
    # Replace the card div with an <a> tag.
    # The start of a card: <div class="bg-white p-8 rounded-2xl border border-lineColor/50 shadow-sm flex flex-col justify-between">
    # There are 4 of them. We'll replace the opening <div> with an <a>
    card_open_regex = re.compile(r'<!-- Card Depoimento (\d+) -->\s*<div class="bg-white p-8 rounded-2xl border border-lineColor/50 shadow-sm flex flex-col justify-between">')
    
    def card_open_repl(match):
        num = match.group(1)
        return f'''<!-- Card Depoimento {num} -->
          <!-- Inserir link da avaliação do Google Maps no href="#" abaixo -->
          <a href="#" target="_blank" rel="noopener" class="block bg-white p-8 rounded-2xl border border-lineColor/50 shadow-sm flex flex-col justify-between hover:shadow-md transition-shadow group">'''
    
    content = card_open_regex.sub(card_open_repl, content)
    
    # Replace the closing </div> of the cards. We need to be careful. The card structure is:
    # <a>
    #   <div>...</div>
    #   <div class="border-t...">...</div>
    # </a> (was </div>)
    # The border-t div is the footer.
    # Let's replace the avatar and the closing div.
    # We can search for the avatar block:
    avatar_regex = re.compile(r'<div class="border-t border-lineColor/50 pt-4 flex items-center gap-3">\s*<div class="w-10 h-10 rounded-full bg-accent1/30 flex items-center justify-center font-bold text-primary font-title">[A-Z]</div>\s*<div>\s*<h4 class="font-semibold text-sm text-titleMain">([^<]+)</h4>\s*</div>\s*</div>\s*</div>')
    
    def avatar_repl(match):
        name = match.group(1)
        return f'''<div class="border-t border-lineColor/50 pt-4 flex items-center gap-3">
              <!-- <img src="caminho/para/foto.jpg" alt="{name}" class="w-10 h-10 rounded-full object-cover"> -->
              <div>
                <h4 class="font-semibold text-sm text-titleMain group-hover:text-primary transition-colors">{name}</h4>
              </div>
            </div>
          </a>'''
    
    content = avatar_regex.sub(avatar_repl, content)

    # 4. WhatsApp links
    # Old link base: https://wa.me/5519981381560 (with or without text)
    # New link: https://wa.me/5519981381560?text=Ol%C3%A1%21+Vim+pelo+site+e+gostaria+de+saber+mais+sobre+os+atendimentos+da+Dahara+Yoga+e+Constela%C3%A7%C3%A3o+Familiar.
    # Let's replace all href="https://wa.me/5519981381560[^"]*"
    new_wa_url = 'https://wa.me/5519981381560?text=Ol%C3%A1%21+Vim+pelo+site+e+gostaria+de+saber+mais+sobre+os+atendimentos+da+Dahara+Yoga+e+Constela%C3%A7%C3%A3o+Familiar.'
    wa_regex = re.compile(r'href="https://wa\.me/5519981381560[^"]*"')
    content = wa_regex.sub(f'href="{new_wa_url}"', content)

    # 6. Footer
    # Find the footer bottom container. Usually it's where "direitos reservados" is.
    # In index.html, it's lines ~1188-1200
    # <div class="border-t border-lineColor/30 py-6 text-center text-sm text-textMain/70 flex flex-col md:flex-row justify-between items-center gap-4">
    #   <p>&copy; 2024 Dahara Yoga e Constelação Familiar. Todos os direitos reservados.</p>
    #   ...
    # </div>
    # We will add the "Projeto desenvolvido em parceria entre AXTRA e Growmni." there.
    footer_regex = re.compile(r'(<p>&copy; 202[45] Dahara Yoga e Constelação Familiar\. Todos os direitos reservados\.</p>)')
    if footer_regex.search(content):
        footer_addition = r'''\1
        <p class="text-xs mt-2 md:mt-0 text-textMain/60">
          Projeto desenvolvido em parceria entre <a href="#" target="_blank" rel="noopener" class="hover:text-primary transition-colors">AXTRA</a> e <a href="#" target="_blank" rel="noopener" class="hover:text-primary transition-colors">Growmni</a>.
        </p>'''
        content = footer_regex.sub(footer_addition, content)
    else:
        # Try finding the div that contains it
        copy_regex = re.compile(r'(<div class="border-t border-lineColor/30 [^>]+>\s*<p>[^<]*Todos os direitos reservados\.</p>)')
        if copy_regex.search(content):
            footer_addition = r'''\1
        <p class="text-xs mt-2 md:mt-0 text-textMain/60">
          Projeto desenvolvido em parceria entre <a href="#" target="_blank" rel="noopener" class="hover:text-primary transition-colors">AXTRA</a> e <a href="#" target="_blank" rel="noopener" class="hover:text-primary transition-colors">Growmni</a>.
        </p>'''
            content = copy_regex.sub(footer_addition, content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Processed {filepath}")

process_html('c:/Users/cleid/Downloads/Antigravity/SITES/site-daharayogaeconstelaçãofamiliar/index.html')
process_html('c:/Users/cleid/Downloads/Antigravity/SITES/site-daharayogaeconstelaçãofamiliar/build/index.html')

