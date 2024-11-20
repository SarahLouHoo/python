class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        '''
        Method to set default values
        '''

        self.__status = False
        self.__mute = False
        self.__channel = Television.MIN_CHANNEL
        self.__volume = Television.MIN_VOLUME


    def power(self)-> None:
        '''
        Method to turn on and off the television
        changes status variable
        '''

        self.__status = not self.__status


    def channel_up(self) -> None:
        '''
        Method to change the channel up when tv is on
        set tv channel to minimum value if this method is called with the
        maximum channel
        '''
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL
    def channel_down(self) -> None:
        '''
        Method to change the channel down when tv is on
        set tv channel to maximum value if this method is called with the
        minimum channel
        '''
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def mute(self) -> None:
        '''
        Method to mute the tv when tv is on
        changes the value of the mute variable
        '''
        if self.__status:
            self.__mute = True

    def volume_up(self) -> None:
        '''
        Method to increase volume when tv is on
        if tv is on maximum volume, do nothing
        unmute first if called while tv is muted
        '''

        if self.__status:
            if self.__mute:
                self.__mute = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        '''
        Method to turn down the volume when tv is on
        if tv is on minimum volume, do nothing
        unmute first if called while tv is muted
        '''
        if self.__status:
            if self.__mute:
                self.__mute = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        '''
        Method to display tv status.
        :return: tv status
        '''

        if self.__mute:
            return f"Power = {self.__status}, Channel = {self.__channel}, Volume = 0"
        else:
            return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"