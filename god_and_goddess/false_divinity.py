
class FalseDivinity:
    def __init__(self):
        self.fraction = []

    def pity(self, love):
        return int(''.join([str(ord(ounce)-69) for ounce in list(love)]))

    def impotent(self, love, fragments: list, scale=3):
        if(scale > 0):
            love = int(love)//23
            self.fraction = [ int(fragment) - (love) for fragment in fragments]
            self.impotent(love, self.fraction, scale-1)
            return self.fraction

    def mortal(self, being):
        return [ chr(essence^2) if essence > 90 else chr(essence^3) for essence in being]

    def inessential(self, encrypted_msg):
        return [encrypted_msg[n:n+7] for n in range(0, len(encrypted_msg), 7)]


if __name__ == "__main__":
    digested_flag = "GKIGKLGI:1201222120121512012381201237120121312011671201224120121712012281201171120123412012361201150120120912012191201236120120912012191201239120122212011761201243"
    key, encrypted_msg = digested_flag.split(":")

    what_god = FalseDivinity()
    raw_love = what_god.pity(key)
    fragments = what_god.inessential(encrypted_msg)
    being = what_god.impotent(raw_love, fragments)
    decrypted_msg = what_god.mortal(being)

    print(''.join(decrypted_msg))



