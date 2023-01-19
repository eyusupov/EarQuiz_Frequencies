from Model.eq_patterns import eqPatterns


class PatternBoxContr:
    def __init__(self, mw_contr):
        self.mw_contr = mw_contr
        self.mw_view = mw_contr.mw_view
        self.mw_view.PatternBox.currentIndexChanged.connect(self.onPatternBoxIndexChanged)
        self.mw_view.NextPatternBut.clicked.connect(self.onNextPatternBut_clicked)
        self.mw_view.PatternBoxView.loadItems(self.getPatternNames())
        self._nextPatternButEnable()

    def onPatternBoxIndexChanged(self, index):
        self.mw_contr.EQContr.setEQMode(mode_num=index + 1)
        self._nextPatternButEnable()

    def onNextPatternBut_clicked(self):
        PBindex = self.mw_view.PatternBox.currentIndex()
        max_index = self.mw_view.PatternBox.count() - 1
        index = PBindex+1 if PBindex < max_index else max_index
        self.mw_view.PatternBox.setCurrentIndex(index)

    def _nextPatternButEnable(self):
        self.mw_view.NextPatternBut.setEnabled(self.mw_view.PatternBox.currentIndex() < self.mw_view.PatternBox.count() - 1)

    @staticmethod
    def getPatternNames():
        return [mode['Name'] for mode in eqPatterns]