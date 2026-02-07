import time

import genanki


MODEL_ID = 1770396438 # timestamp

my_model = genanki.Model(
  MODEL_ID,
  'Arcs Game Card',
  fields=[
    {'name': 'FrontImage'},
    {'name': 'BackImage'},
  ],
  templates=[
    {
      'name': 'Arcs Card',
      'qfmt': '{{FrontImage}}',
      'afmt': '{{BackImage}}',
    },
  ],
  css=''
)

# collecting decks and media files
decks = []
media_files = set()

def add_to_deck(deck, fnames):
    for fname in fnames:
        front = f"blur_{fname}"
        back = fname
        media_files.add(f"imgs/{front}")
        media_files.add(f"imgs/{back}")

        note = genanki.Note(
          model=my_model,
          fields=[
              f'<img src="{front}">',
              f'<img src="{back}">',
          ]
        )
        deck.add_note(note)

# 1) base court cards (guild & vox)
bc = genanki.Deck(MODEL_ID + 1, 'Arcs::BaseCourt')
add_to_deck(bc, [f"BC{i:02d}.png" for i in range(1, 31 + 1)])
decks.append(bc)

# 2) base leader
lead_base = genanki.Deck(MODEL_ID + 2, 'Arcs::Leader::Base')
add_to_deck(lead_base, [f"LEAD{i:02d}.png" for i in range(1, 8 + 1)])
decks.append(lead_base)

# 3) base lore
lore_base = genanki.Deck(MODEL_ID + 3, 'Arcs::Lore::Base')
add_to_deck(lore_base, [f"L{i:02d}.png" for i in range(1, 14 + 1)])
decks.append(lore_base)

# 4) L&L leader
lead_ll = genanki.Deck(MODEL_ID + 4, 'Arcs::Leader::LL')
add_to_deck(lead_ll, [f"LEAD{i:02d}.png" for i in range(9, 16 + 1)])
decks.append(lead_ll)

# 5) L&L lore
lore_ll = genanki.Deck(MODEL_ID + 5, 'Arcs::Lore::LL')
add_to_deck(lore_ll, [f"L{i:02d}.png" for i in range(15, 28 + 1)])
decks.append(lore_ll)

# Save the deck to a file with images included
genanki.Package(decks, media_files=media_files).write_to_file('Arcs_Cards.apkg')
