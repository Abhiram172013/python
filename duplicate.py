studentdetails={'id1':
                {'name':['abhiram'],
                 'class':['VII'],
                 'subject':['maths,computer']
                  },
                  'id2':
                {'name':['ronaldo'],
                 'class':['VII'],
                 'subject':['maths,computer']
                  },
                'id3':
                {'name':['mbappe'],
                 'class':['VII'],
                 'subject':['maths,computer']
                  },
                'id4':
                {'name':['abhiram'],
                 'class':['VII'],
                 'subject':['maths,computer']
                  },
                }
result={}
for key,value in studentdetails.items():
    if value not in result.values():
        result[key]=value
print(result)