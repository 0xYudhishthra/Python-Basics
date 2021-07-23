def convertDatasetsToInsertIntoStatements(datasetFilename,sqlTableName=None):
    individualRecords = []
    temp = []
    finalList = []
    columnDataTypes = []
    with open(datasetFilename,mode='r') as datasetCSV:
        datasetCSV.seek(3)
        for row in datasetCSV:
            columnNames = (row.strip().split(","))
            break
        for row in datasetCSV:
            individualRecords.append(row.strip('\n').split(","))
    for columnName in columnNames:
       for char in columnName:
           if char.startswith("("):
               columnDataTypes.append(columnName[columnName.index(char)+1:columnName.index(columnName[-1])])
    count = 0
    for data in individualRecords:
        for subData in data:
            dataType = columnDataTypes[count]
            if (
                dataType in ("int", "decimal")
                and subData == ''
                or dataType not in ("int", "decimal")
                and dataType in ("char", "varchar", "date")
                and subData == ''
            ): 
                temp.append('NULL')
            elif dataType in ("int", "decimal"):
                temp.append(subData)
            elif dataType in ("char", "varchar", "date"):
                temp.append(f"'{subData}'")
            count += 1
            if count == len(columnDataTypes):
                finalList.append(temp)
                temp = []
                count = 0
                break
        continue
    with open("pasteTheseStatementsInSqlServer.txt", mode="w") as f:
        f.write(f'INSERT INTO {sqlTableName.upper()}\n')
        f.write('VALUES\n')
        for data in finalList:
            f.write('({}),\n'.format(",".join(data)))
            if data == finalList[-1]:
                f.write('({});\nGO'.format(",".join(data)))


'''
Just edit this part for your own usage
'''

convertDatasetsToInsertIntoStatements(
    'propertyDataset.csv',  #Replace this with the name of the excel file that you downloaded in CSV format
    'property'              #Replace this with the name of your table
)

