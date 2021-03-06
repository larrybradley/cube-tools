def setup():

    from . import loaders
    from . import subset_ops
    from . import viewers
    from . import tools
    from . import clients

    from glue.config import qt_client
    from .qt.spectra_widget import SpectraWindow
    qt_client.add(SpectraWindow)

    from .qt.table_widget import TableWindow
    qt_client.add(TableWindow)
