import re

txt = """Non tempora amet 1994-02-24 18:26:25.680292 est. Sed dolor labore ut labore velit porro tempora. Quisquam 
dolor non voluptatem. Numquam quiquia adipisci dolore eius numquam amet voluptatem. Adipisci 2010-09-15 
14:39:40.982917 non sed est quiquia dolore quisquam est. Ut tempora quisquam amet  1998-03-16 16:14:16.647591 
quisquam amet numquam.  2006-02-04 09:14:57.833855 Aliquam dolor quisquam neque eius dolorem. Dolore velit amet 
quaerat consectetur dolor velit. Sed adipisci 2017-05-01 00:25:34.398268 eius dolorem magnam. Etincidunt adipisci 
2000-09-17 15:29:24.527475 sit numquam dolor velit d 2013-01-11 21:58:55.007595 olorem eius.\n\nSit numquam dolor 
velit neque. 2010-11-14 05:14:47.704542 Sed etincidunt numquam 1994-01-14 03:42:59.505113 neque non sit velit. 
Quiquia numquam adipisci adipisci sed est etincidunt. """

time_pattern = r"((\d{2}):(\d{2}):(\d{2})(.\d+)?)"
for time_match in re.finditer(time_pattern, txt):
    print()
    print('Time:', time_match)
    print('Groups:', time_match.groups())
    print('Hour:', time_match.group(2))
    print('Minute:', time_match.group(3))
    print('Second:', time_match.group(4))
    print('Nano_secs:', time_match.group(5))
