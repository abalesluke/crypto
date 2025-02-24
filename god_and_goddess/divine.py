

class Divinity:
    def __init__(self, being):
        self.being = being
        self.fraction = []
        self.love = ''
        self.sequence_1 = 0
        self.sequence_2 = 0


    def pity(self, love):
        self.love = ''.join([chr(int(ounce)+69) for ounce in list(love)])


    def omnipotence(self, fragments: list, scale=3):
        self.pity(str(sum(fragments)))
        if(scale == 3):
            self.sequence_1 = sum(fragments)

        elif(scale == 2):
            self.sequence_2 = sum(fragments)
        elif(scale == 1):
            print(f"Love Sequence: {self.sequence_1}, {self.sequence_2}")

        if(scale > 0):
            self.fraction = [ fragment + sum(fragments) for fragment in fragments]
            self.omnipotence(self.fraction, scale-1)
            return self.fraction


    def immortal(self):
        return self.omnipotence([ ord(essence)^2 if ord(essence) > 90 else ord(essence)^3 for essence in self.being])


if __name__=="__main__":
    flag = "hax{demo_flag_redacted}" # This is not the actual flag.

    god = Divinity(flag)
    immortality = god.immortal()
    integral = ''.join([ str(i) for i in immortality])
    unity = god.love

    digested_flag = f"Digested flag: {unity}:{integral}"
    print(digested_flag)

    # Love Sequence: 2172, 49956
    # Digested flag: GKIGKLGI:1201222120121512012381201237120121312011671201224120121712012281201171120123412012361201150120120912012191201236120120912012191201239120122212011761201243


