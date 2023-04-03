from GUI.Playlist.plsong import PlSong
from Model.globals import MinAudioDuration
from Model.AudioEngine.preview_audio import PreviewAudioCrop
from GUI.Modes.PreviewMode import PreviewMode


class AudioLoad:
    def __init__(self, parent):     # parent: MainWindowContr
        self.parent = parent
        self.mw_view = self.parent.mw_view
        self.TransportContr = self.parent.TransportContr

    def _songCanBeLoaded(self, Song: PlSong):
        if self.parent.CurrentSourceMode.name != 'Audiofile':
            return False
        if hasattr(Song, 'file_properties'):
            Song.__delattr__('file_properties')
        return bool(
            Song.duration >= MinAudioDuration
            and Song.exists
            and Song.samplerate >= 44100
        )

    def _switchToPreview(self):
        if self.parent.CurrentMode.name == 'Preview':
            self.parent.CurrentMode.updateCurrentAudio()
        elif self.mw_view.actionPreview_Mode.isChecked():
            self.parent.CurrentMode = PreviewMode(self.parent)
        else:
            self.mw_view.actionPreview_Mode.setChecked(True)

    def load_song(self, Song: PlSong, forcePlayAfter=False):
        if not self._songCanBeLoaded(Song):
            return
        reloaded_same = (self.parent.SourceAudio is not None and self.parent.SourceAudio == Song)
        reloaded_same_path = (self.parent.SourceAudio is not None and self.parent.SourceAudio.path == Song.path)
        if not reloaded_same_path:
            self.parent.SRC.savePrevSourceAudioRange()
        self.parent.SourceAudio = Song
        self.parent.PlaylistContr.PlNavi.setCurrentSong(Song)
        self.parent.playAudioOnPreview = True if reloaded_same \
            else self.mw_view.actionStartPlayingAfterLoading.isChecked()
        self._switchToPreview()
        if reloaded_same_path:
            if not reloaded_same:
                self.TransportContr.PlayerContr.setCurrentSongToPlaylistModel()
            self.TransportContr.PlayerContr.onStopTriggered()
            self.TransportContr.PlayerContr.play()
            return
        self.parent.ADGen = None
        self.TransportContr.PlayerContr.loadCurrentAudio(play_after=self.parent.playAudioOnPreview or forcePlayAfter)

    def load_pinknoise(self):
        self.parent.SourceAudio = PlSong('pinknoise')
        self.TransportContr.TransportView.setHeader('Pink noise')
        dur = self.parent.SourceAudio.duration
        self.parent.SourceRange = PreviewAudioCrop(dur, 0, dur, self.TransportContr.TransportView.SliceLenSpin.value())
        self.TransportContr.setInitCropRegionView()
        self.TransportContr.TransportView.setDurationLabValue(dur)
        self.TransportContr.TransportView.AudioSliderView.setNewDataLength(dur)

    def setNoAudio(self):
        self.TransportContr.PlayerContr.onStopTriggered(checkPlaybackState=True)
        self.parent.SourceAudio = self.parent.LastSourceAudio = None
        self.parent.ADGen = None
        self.parent.CurrentAudio = None
        self.parent.LoadedFileHash = None
        self.parent.SRC.disconnectSourceRangeSig()
        self.TransportContr.PlayerContr.clearSource()
        self.parent.CurrentMode.cleanTempAudio()
        self.parent.LoadedFilePath = None
        self.mw_view.TransportPanelView.noSongState()
        self.parent.SourceRange = None
        self.parent.setMakeAudioActionsEnabled(False)
        self.mw_view.status.clearMessage()
