h1_text = 'Input field'
invalid_result_string = 'Enter a valid string consisting of letters, numbers, underscores or hyphens.'
invalid_result_1_string = 'Please enter 2 or more characters'
invalid_result_25_string = 'Please enter no more than 25 characters'
invalid_result_password = 'Low password complexity'
invalid_result_email = 'Enter a valid email address.'
validPayloadSimple = ['Hello_World', 'bla-bla',
                      '1313131', '--___--']
invalidPayloadSimple = ['bla bla',
                        'аыаыаыаы',
                        '$%@&$&!',
                        'sgsg$@']
invalid1PayloadSimple = '1'
invalid25PayloadSimple = ['more_then_twenty_five_symbols']


validPayloadEmail = ['test@gmail.com',
                     'fbuwbfwubfiwnfjwifniwifwbfiwbfbiwfiwfbbwifwbfwbfiw@gmail.com',
                     'test123131@gmail.com',
                     '1@mail.ru',
                     'pochta@rambler.ru']
invalidPayloadEmail = ['test@mailru',
                       'testmail.ru',
                       'testmailru']


validPayloadPassword = ['Pass111!',
                        'Pp1!fwebfguwbguwybguysbkghSBUGbsbghsBFsywugvwigubSK',
                        'PASs111!']
invalidPayloadPassword = ['FQUFUYQUYFQUFQF',
                          'bgsisbgisbgiubsigbs',
                          '3412341242424214141',
                          'Passw1!',
                          'FQFBQYBFifbqibfqb',
                          '$*&!@$^*&!@^$*!']

