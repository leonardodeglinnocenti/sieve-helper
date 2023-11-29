

class SieveUtilities():

    def generate_sieve_config(config):
        # config has shape [email, from_check, to_check, target_folder]
        out_string = "require \"fileinto\";"

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


