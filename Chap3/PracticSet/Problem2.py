letter = ''' 
          Dear <|Name|>,
          You are Birthday!
          <|Date|>
            '''

print(letter.replace("<|Name|>", "Sandhya").replace("<|Date|>", "27"))