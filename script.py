import pandas as pd
import numpy as np
import os

#path_to_target_directory_inside_container -> docker run --mount src=path_to_source_directory_inside_host,target=path_to_target_directory_inside_container,type=bind
path_images = '/images'

path, dirs, files = next(os.walk(path_images))
file_count = len(files)

print("% has %s images" % (path_images, file_count))

rows = 9955
random_tags = np.random.randint(16, size=rows)
solution = pd.DataFrame(data=random_tags, index = list(range(rows)), columns = ['tag'])
solution.to_csv('solution.csv')
