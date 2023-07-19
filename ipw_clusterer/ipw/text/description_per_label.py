def description_per_label(df, model, run):
    label_column = model.col(run)

    returnvalue = {}

    for i in df.index:
        label = df.loc[i, label_column]
        description = df.loc[i, 'description']
        
        if label in returnvalue:
            returnvalue[label] = returnvalue[label] + '. '+ description
        else:
            dict = {}
            returnvalue[label] = description

    return returnvalue