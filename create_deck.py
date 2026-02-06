import time

import genanki


MODEL_ID = 1770396438 # timestamp
DECK_ID = MODEL_ID + 1

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

# first deck: base court cards (guild & vox)
arcs_bc = genanki.Deck(
  DECK_ID,
  'Arcs::BaseCourt'
)
fnames = [f"BC{i:02d}.png" for i in range(1, 31 + 1)]
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
    arcs_bc.add_note(note)
decks.append(arcs_bc)

# Save the deck to a file with images included
genanki.Package(decks, media_files=media_files).write_to_file('Arcs_BaseCourt.apkg')
