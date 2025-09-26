import threading

class H2O(object):
    def __init__(self):
        # Semaphores ensure that in each "molecule cycle":
        # - Only 2 hydrogens may enter
        # - Only 1 oxygen may enter
        self.h_sem = threading.Semaphore(2)   # hydrogen permits
        self.o_sem = threading.Semaphore(1)   # oxygen permits

        # Condition variable + counter simulate a barrier
        self.lock = threading.Lock()
        self.cv = threading.Condition(self.lock)
        self.arrived = 0  # counts how many threads (H or O) have arrived for the current molecule

    def _finish_or_wait(self):
        """
        Shared barrier logic:
        - Each thread calls this after 'bonding' (printing H or O).
        - First 2 threads wait.
        - The 3rd thread resets for the next molecule and wakes the others.
        """
        with self.cv:
            self.arrived += 1

            if self.arrived == 3:
                # We have 3 threads = 1 full molecule formed
                # Reset the counter for the next molecule
                self.arrived = 0

                # Replenish the permits: 2 hydrogens + 1 oxygen
                self.h_sem.release()
                self.h_sem.release()
                self.o_sem.release()

                # Wake up the other two waiting threads
                self.cv.notify_all()
            else:
                # Wait until the 3rd thread does the reset
                while self.arrived != 0:
                    self.cv.wait()

    def hydrogen(self, releaseHydrogen):
        """
        :type releaseHydrogen: Callable[[], None]
        Hydrogen thread calls this method.
        """
        self.h_sem.acquire()   # ensures at most 2 hydrogens participate in current molecule
        releaseHydrogen()      # "bond" (print 'H')
        self._finish_or_wait() # synchronize with O and the other H

    def oxygen(self, releaseOxygen):
        """
        :type releaseOxygen: Callable[[], None]
        Oxygen thread calls this method.
        """
        self.o_sem.acquire()   # ensures at most 1 oxygen participates in current molecule
        releaseOxygen()        # "bond" (print 'O')
        self._finish_or_wait() # synchronize with 2 Hs
