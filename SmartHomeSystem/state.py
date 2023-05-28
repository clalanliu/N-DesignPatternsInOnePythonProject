import logging

from SmartHomeSystem import SmartDevice

logger = logging.getLogger(__name__)


class SmartLockState:
    def enter_pin(self, pin, lock):
        pass

    def lock(self, lock):
        pass

    def unlock(self, lock):
        pass


class LockedState(SmartLockState):
    def enter_pin(self, pin, lock):
        if pin == lock.correct_pin:
            logger.info("Correct PIN entered. Unlocking the smart lock.")
            lock.change_state(UnlockedState())
        else:
            logger.info("Incorrect PIN entered. The smart lock remains locked.")

    def lock(self, lock):
        logger.info("The smart lock is already locked.")

    def unlock(self, lock):
        logger.info("Unlock the smart lock first before trying to lock it again.")


class UnlockedState(SmartLockState):
    def enter_pin(self, pin, lock):
        logger.info("The smart lock is already unlocked.")

    def lock(self, lock):
        logger.info("Locking the smart lock.")
        lock.change_state(LockedState())

    def unlock(self, lock):
        logger.info("The smart lock is already unlocked.")


class SmartLock(SmartDevice):
    def __init__(self, correct_pin):
        self.correct_pin = correct_pin
        self.state = LockedState()

    def change_state(self, state):
        self.state = state

    def enter_pin(self, pin):
        self.state.enter_pin(pin, self)

    def lock(self):
        self.state.lock(self)

    def unlock(self):
        self.state.unlock(self)
