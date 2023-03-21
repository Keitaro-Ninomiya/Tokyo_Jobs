Steps for OCR
#Download and Organize#
1. Choose Year
2. Create Page list /Data_Collection/Index
3. Edit page list: Manually
4. Download Documents /Data_Collection/Download_Image

##Split Step##(1h)
1. Split page into two /Data_Collection/Split_Page
**Check the starting and ending page of the raw directory**
**Make sure to prepare folders before saving splitted image **
2. Check the list the pages failed layout detection
3. Fix errors

#Insert Department Level info into final dataframe#(0h)
1. Create dataframe for storing data /Data_Collection/Split_Department

#Create directories
1. Create seperate directories for each department and offices.
/Data_Collection/Create_Directories

#Split into Office Level#
1. Detect starting location of a office /Data_Collection/Split_Office/Code
2. Crop images into office level and save to directory /Data_Collection/Split_Office/Code2

##Split into unit level: 1938-1942#
#1. Detect starting location of a office /Data_Collection/Split_Unit/Code
#2. Create seperate directories for each units. /Data_Collection/Create_Unit/Code
#3. Crop images into unit level and save to directory /Data_Collection/Split_Unit/Code2

##Split into position level: -1937#
#1. Detect names of positions and starting location of each positions in each office /Data_Collection/Split_Position1/Code
#2. Create seperate directories for each positions /Data_Collection/Create_Position/Code
#3. Crop images into position level and save to directory  /Data_Collection/Split_Position1/Code2

##Extract Data#
#1. Extract data /Data_Collection/Extract Data

-----------------------------------------------------------------------
##Split into unit level: 1943-#
#1. Detect starting location of a office /Data_Collection/Split_Position3
#
