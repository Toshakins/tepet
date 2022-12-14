from unittest.mock import patch


class PatchMixin(object):
    def _patch(self, *args, **kwargs):
        patcher = patch.object(*args, **kwargs)
        patched_entity = patcher.start()
        self.addCleanup(patcher.stop)
        return patched_entity
