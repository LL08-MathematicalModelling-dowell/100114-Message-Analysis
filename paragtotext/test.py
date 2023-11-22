# import re
#
# def organize_text_by_time(input_text):
#     dialogue_info = {}
#     time_pattern = r'\d{1,2}:\d{2}[apmAPM]{2}'
#
#     matches = re.finditer(time_pattern, input_text)
#     matches = [match.group() for match in matches]
#
#     # Split the input text using time as a delimiter
#     segments = re.split(time_pattern, input_text)
#     segments = [segment.strip() for segment in segments]
#
#     for time, text in zip(matches, segments[1:]):  # Skip the first empty segment
#         dialogue_info[time] = {"text": text + ' ' + segments[0]}
#
#     return dialogue_info
#
# input_text = """
# Nadeem — 9:24am
# Joint diplomatic statement issued by multiple countries' governments concerning recent violence and gatherings.
# Jacobninandowell — 9:45am
# This is concerning.
#
# """
#
# # Call the function with the input text
# result = organize_text_by_time(input_text)
#
# # Print the organized information in the desired format
# print(result)
#
# import re
#
# input_text = """
# Nadeem — 9:24am
# Joint diplomatic statement issued by multiple countries' governments concerning recent violence and gatherings.
# Jacobninandowell — 9:45am
# This is concerning.
# """
#
# time_pattern = r'\b\d{1,2}:\d{2}[apmAPM]{2}'
#
# matches = re.findall(f"{time_pattern}\s*(.*?)(?={time_pattern}|$)", input_text, re.DOTALL)
# dialogue_info = {time.group(0): text.strip() for time, text in zip(re.finditer(time_pattern, input_text), matches)}
#
# print(dialogue_info)
