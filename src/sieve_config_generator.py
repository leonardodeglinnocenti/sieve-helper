

class SieveUtilities():

    def generate_sieve_config(config):
        # config has shape [email, from_check, to_check, target_folder]
        out_string = "require \"fileinto\";"
    #the following loop loops through the config array and adds the sieve rules to the out_string
        for c in config:
            email = c[0]
            from_check = c[1]
            to_check = c[2]
            target_folder = c[3]

            if from_check and to_check:
                out_string += "if address :is [\"From\", \"To\"] \""
            elif from_check and not to_check:
                out_string += "if address :is [\"From\"] \""
            else:
                out_string += "if address :is [\"To\"] \""
            out_string += email
            out_string += "\"{\" {fileinto \""
            out_string += target_folder
            out_string += "\";}"

        return out_string
    # New version of sieve config where config is not an array, but an object with keys

    def new_generate_sieve_config(config):
        # config has attributes config.email config.from_check config.to_check config.target_folder
        out_string = "require \"fileinto\";"


