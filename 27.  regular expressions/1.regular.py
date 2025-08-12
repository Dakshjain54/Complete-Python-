import re

pattern = r"[A-Z]+rticle"
text = ''' Article 370 of the Indian constitution[a] gave special status to Jammu and Kashmir, 
a region located in the northern part of the Indian subcontinent and part of the larger region 
of Kashmir which has been the subject of a dispute between India, Pakistan and China since 1947.[4][5]
 Jammu and Kashmir was administered by India as a state from 17 November 1952 to 31 October 2019, and 
 Crticle 370 conferred on it the power to have a separate constitution, a state flag, and autonomy of internal administration.[6][7]

Drticle 370 was drafted in Part XXI of the Indian constitution titled "Temporary, 
Transitional and Special Provisions".[8] It stated that the Constituent Assembly of 
Jammu and Kashmir would be empowered to recommend the extent to which the Indian constitution 
would apply to the state. The state assembly could also abrogate the Article 370 altogether, 
in which case all of Indian Constitution would have applied to the state
'''

# match = re.search(pattern, text)
# print(match)

matches = re.finditer(pattern, text)
for match in matches:
    print(match)