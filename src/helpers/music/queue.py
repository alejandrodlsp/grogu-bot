from discord.ext import commands
import random
from enum import Enum

class QueueIsEmptyError(commands.CommandError):
    pass

class QueueRepeatMode(Enum):
    NONE = 0
    ONE = 1
    ALL = 2

class Queue:
    def __init__(self):
        self._queue = []
        self.position = 0
        self.repeat_mode = QueueRepeatMode.NONE

    def add(self, *args):
        self._queue.extend(args)

    @property
    def is_empty(self):
        return not self._queue
        
    @property
    def first_track(self):
        if not self._queue:
            raise QueueIsEmptyError
        return self._queue[0]

    @property
    def current_track(self):
        if not self._queue:
            raise QueueIsEmptyError
        if self.position <= len(self._queue) - 1:
            return self._queue[self.position]

    @property
    def upcoming(self):
        if not self._queue:
            raise QueueIsEmptyError
        return self._queue[self.position + 1:] 

    @property
    def history(self):
        if not self._queue:
            raise QueueIsEmptyError
        return self._queue[:self.position]

    @property
    def length(self):
        return len(self._queue)

    def empty(self):
        self._queue.clear()
        self.position = 0

    def get_next_track(self):
        if not self._queue:
            raise QueueIsEmptyError
        self.position += 1

        if self.position < 0:
            return None
        elif self.position > len(self._queue) - 1:
            if self.repeat_mode == QueueRepeatMode.ALL:
                self.position = 0
            else:
                return None

        return self._queue[self.position]

    def shuffle(self):
        if not self._queue:
            raise QueueIsEmptyError
        
        upcoming = self.upcoming
        random.shuffle(upcoming)
        self._queue = self._queue[:self.position + 1]
        self._queue.extend(upcoming)

    def set_repeat_mode(self, mode):
        if mode == 'NONE':
            self.repeat_mode = QueueRepeatMode.NONE
        elif mode == '1':
            self.repeat_mode = QueueRepeatMode.ONE
        elif mode == 'ALL':
            self.repeat_mode = QueueRepeatMode.ALL
        