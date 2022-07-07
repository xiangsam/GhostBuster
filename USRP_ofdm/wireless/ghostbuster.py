#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: ghostbuster
# Description: wireless
# GNU Radio version: 3.9.5.0

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import analog
from gnuradio import blocks
from gnuradio import digital
from gnuradio import fft
from gnuradio.fft import window
from gnuradio import gr
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio import uhd
import time
from gnuradio.digital.utils import tagged_streams
import pmt



from gnuradio import qtgui

class ghostbuster(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "ghostbuster", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("ghostbuster")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "ghostbuster")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.pilot_symbols = pilot_symbols = ((1, 1, 1, -1,),)
        self.pilot_carriers = pilot_carriers = ((-21, -7, 7, 21,),)
        self.payload_mod = payload_mod = digital.constellation_qpsk()
        self.packet_length_tag_key = packet_length_tag_key = "packet_len"
        self.occupied_carriers = occupied_carriers = ([-26, -25, -24, -23, -22, -20, -19, -18, -17, -16, -15, -14, -13, -12, -11, -10, -9, -8, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 22, 23, 24, 25, 26],)
        self.length_tag_key = length_tag_key = "frame_len"
        self.header_mod = header_mod = digital.constellation_bpsk()
        self.fft_len = fft_len = 64
        self.sync_word2 = sync_word2 = [0j, 0j, 0j, 0j, 0j, 0j, (-1+0j), (-1+0j), (-1+0j), (-1+0j), (1+0j), (1+0j), (-1+0j), (-1+0j), (-1+0j), (1+0j), (-1+0j), (1+0j), (1+0j), (1 +0j), (1+0j), (1+0j), (-1+0j), (-1+0j), (-1+0j), (-1+0j), (-1+0j), (1+0j), (-1+0j), (-1+0j), (1+0j), (-1+0j), 0j, (1+0j), (-1+0j), (1+0j), (1+0j), (1+0j), (-1+0j), (1+0j), (1+0j), (1+0j), (-1+0j), (1+0j), (1+0j), (1+0j), (1+0j), (-1+0j), (1+0j), (-1+0j), (-1+0j), (-1+0j), (1+0j), (-1+0j), (1+0j), (-1+0j), (-1+0j), (-1+0j), (-1+0j), 0j, 0j, 0j, 0j, 0j]
        self.sync_word1 = sync_word1 = [0., 0., 0., 0., 0., 0., 0., 1.41421356, 0., -1.41421356, 0., 1.41421356, 0., -1.41421356, 0., -1.41421356, 0., -1.41421356, 0., 1.41421356, 0., -1.41421356, 0., 1.41421356, 0., -1.41421356, 0., -1.41421356, 0., -1.41421356, 0., -1.41421356, 0., 1.41421356, 0., -1.41421356, 0., 1.41421356, 0., 1.41421356, 0., 1.41421356, 0., -1.41421356, 0., 1.41421356, 0., 1.41421356, 0., 1.41421356, 0., -1.41421356, 0., 1.41421356, 0., 1.41421356, 0., 1.41421356, 0., 0., 0., 0., 0., 0.]
        self.samp_rate = samp_rate = 2000000
        self.payload_equalizer = payload_equalizer = digital.ofdm_equalizer_simpledfe(fft_len, payload_mod.base(), occupied_carriers, pilot_carriers, pilot_symbols, 1)
        self.packet_len = packet_len = 96
        self.header_formatter = header_formatter = digital.packet_header_ofdm(occupied_carriers, n_syms=1, len_tag_key=packet_length_tag_key, frame_len_tag_key=length_tag_key, bits_per_header_sym=header_mod.bits_per_symbol(), bits_per_payload_sym=payload_mod.bits_per_symbol(), scramble_header=False)
        self.header_equalizer = header_equalizer = digital.ofdm_equalizer_simpledfe(fft_len, header_mod.base(), occupied_carriers, pilot_carriers, pilot_symbols)
        self.freq = freq = 5.08e9
        self.band_width = band_width = 6e6

        ##################################################
        # Blocks
        ##################################################
        self.uhd_usrp_source_1_0 = uhd.usrp_source(
            ",".join(("serial = 31FBCB0", '')),
            uhd.stream_args(
                cpu_format="fc32",
                args='',
                channels=list(range(0,2)),
            ),
        )
        self.uhd_usrp_source_1_0.set_subdev_spec('A:0 B:0', 0)
        self.uhd_usrp_source_1_0.set_samp_rate(samp_rate)
        self.uhd_usrp_source_1_0.set_time_now(uhd.time_spec(time.time()), uhd.ALL_MBOARDS)

        self.uhd_usrp_source_1_0.set_center_freq(freq, 0)
        self.uhd_usrp_source_1_0.set_antenna("RX2", 0)
        self.uhd_usrp_source_1_0.set_bandwidth(band_width, 0)
        self.uhd_usrp_source_1_0.set_gain(40, 0)
        self.uhd_usrp_source_1_0.set_auto_dc_offset(True, 0)

        self.uhd_usrp_source_1_0.set_center_freq(freq, 1)
        self.uhd_usrp_source_1_0.set_antenna("RX2", 1)
        self.uhd_usrp_source_1_0.set_bandwidth(band_width, 1)
        self.uhd_usrp_source_1_0.set_gain(40, 1)
        self.uhd_usrp_source_1_0.set_auto_dc_offset(True, 1)
        self.qtgui_sink_x_0_1 = qtgui.sink_c(
            1024, #fftsize
            window.WIN_BLACKMAN_hARRIS, #wintype
            freq, #fc
            band_width, #bw
            "", #name
            True, #plotfreq
            True, #plotwaterfall
            True, #plottime
            True, #plotconst
            None # parent
        )
        self.qtgui_sink_x_0_1.set_update_time(1.0/10)
        self._qtgui_sink_x_0_1_win = sip.wrapinstance(self.qtgui_sink_x_0_1.qwidget(), Qt.QWidget)

        self.qtgui_sink_x_0_1.enable_rf_freq(False)

        self.top_layout.addWidget(self._qtgui_sink_x_0_1_win)
        self.qtgui_sink_x_0_0 = qtgui.sink_c(
            1024, #fftsize
            window.WIN_BLACKMAN_hARRIS, #wintype
            freq, #fc
            band_width, #bw
            "", #name
            True, #plotfreq
            True, #plotwaterfall
            True, #plottime
            True, #plotconst
            None # parent
        )
        self.qtgui_sink_x_0_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_0_win = sip.wrapinstance(self.qtgui_sink_x_0_0.qwidget(), Qt.QWidget)

        self.qtgui_sink_x_0_0.enable_rf_freq(False)

        self.top_layout.addWidget(self._qtgui_sink_x_0_0_win)
        self.fft_vxx_0_0 = fft.fft_vcc(fft_len, True, (), True, 1)
        self.fft_vxx_0 = fft.fft_vcc(fft_len, True, (), True, 1)
        self.digital_packet_headerparser_b_0_0 = digital.packet_headerparser_b(header_formatter.base())
        self.digital_packet_headerparser_b_0 = digital.packet_headerparser_b(header_formatter.base())
        self.digital_ofdm_sync_sc_cfb_0_0 = digital.ofdm_sync_sc_cfb(fft_len, fft_len//4, False, 0.9)
        self.digital_ofdm_sync_sc_cfb_0 = digital.ofdm_sync_sc_cfb(fft_len, fft_len//4, False, 0.9)
        self.digital_ofdm_serializer_vcc_header_0 = digital.ofdm_serializer_vcc(fft_len, occupied_carriers, length_tag_key, '', 0, '', True)
        self.digital_ofdm_serializer_vcc_header = digital.ofdm_serializer_vcc(fft_len, occupied_carriers, length_tag_key, '', 0, '', True)
        self.digital_ofdm_frame_equalizer_vcvc_0_0 = digital.ofdm_frame_equalizer_vcvc(header_equalizer.base(), fft_len//4, length_tag_key, True, 1)
        self.digital_ofdm_frame_equalizer_vcvc_0 = digital.ofdm_frame_equalizer_vcvc(header_equalizer.base(), fft_len//4, length_tag_key, True, 1)
        self.digital_ofdm_chanest_vcvc_0_0 = digital.ofdm_chanest_vcvc(sync_word1, sync_word2, 1, 0, 3, False)
        self.digital_ofdm_chanest_vcvc_0 = digital.ofdm_chanest_vcvc(sync_word1, sync_word2, 1, 0, 3, False)
        self.digital_header_payload_demux_0_0 = digital.header_payload_demux(
            3,
            fft_len,
            fft_len//4,
            length_tag_key,
            "",
            True,
            gr.sizeof_gr_complex,
            "rx_time",
            samp_rate,
            (),
            0)
        self.digital_header_payload_demux_0 = digital.header_payload_demux(
            3,
            fft_len,
            fft_len//4,
            length_tag_key,
            "",
            True,
            gr.sizeof_gr_complex,
            "rx_time",
            samp_rate,
            (),
            0)
        self.digital_constellation_decoder_cb_0_0 = digital.constellation_decoder_cb(header_mod.base())
        self.digital_constellation_decoder_cb_0 = digital.constellation_decoder_cb(header_mod.base())
        self.blocks_multiply_xx_0_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_file_sink_8_0 = blocks.file_sink(gr.sizeof_gr_complex*64, '/home/samrito/workarea/OFDM0516/0520_seperate/payload_streamAB', False)
        self.blocks_file_sink_8_0.set_unbuffered(False)
        self.blocks_file_sink_8 = blocks.file_sink(gr.sizeof_gr_complex*64, '/home/samrito/workarea/OFDM0516/0520_seperate/payload_streamAA', False)
        self.blocks_file_sink_8.set_unbuffered(False)
        self.blocks_file_sink_1_0_0 = blocks.file_sink(gr.sizeof_gr_complex*1, '/home/samrito/workarea/OFDM0516/0520_seperate/afterChannelAA', False)
        self.blocks_file_sink_1_0_0.set_unbuffered(False)
        self.blocks_file_sink_1_0 = blocks.file_sink(gr.sizeof_gr_complex*1, '/home/samrito/workarea/OFDM0516/0520_seperate/afterChannelAB', False)
        self.blocks_file_sink_1_0.set_unbuffered(False)
        self.blocks_file_sink_0_0 = blocks.file_sink(gr.sizeof_gr_complex*1, '/home/samrito/workarea/OFDM0516/0520_seperate/beforeDemuxAB', False)
        self.blocks_file_sink_0_0.set_unbuffered(False)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_gr_complex*1, '/home/samrito/workarea/OFDM0516/0520_seperate/beforeDemuxAA', False)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.blocks_delay_0_0 = blocks.delay(gr.sizeof_gr_complex*1, fft_len+fft_len//4)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_gr_complex*1, fft_len+fft_len//4)
        self.analog_frequency_modulator_fc_0_0 = analog.frequency_modulator_fc(-2.0/fft_len)
        self.analog_frequency_modulator_fc_0 = analog.frequency_modulator_fc(-2.0/fft_len)


        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.digital_packet_headerparser_b_0, 'header_data'), (self.digital_header_payload_demux_0, 'header_data'))
        self.msg_connect((self.digital_packet_headerparser_b_0_0, 'header_data'), (self.digital_header_payload_demux_0_0, 'header_data'))
        self.connect((self.analog_frequency_modulator_fc_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.analog_frequency_modulator_fc_0_0, 0), (self.blocks_multiply_xx_0_0, 0))
        self.connect((self.blocks_delay_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.blocks_delay_0_0, 0), (self.blocks_multiply_xx_0_0, 1))
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.digital_header_payload_demux_0, 0))
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.blocks_file_sink_0_0, 0))
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.digital_header_payload_demux_0_0, 0))
        self.connect((self.digital_constellation_decoder_cb_0, 0), (self.digital_packet_headerparser_b_0, 0))
        self.connect((self.digital_constellation_decoder_cb_0_0, 0), (self.digital_packet_headerparser_b_0_0, 0))
        self.connect((self.digital_header_payload_demux_0, 1), (self.blocks_file_sink_8, 0))
        self.connect((self.digital_header_payload_demux_0, 0), (self.fft_vxx_0, 0))
        self.connect((self.digital_header_payload_demux_0_0, 1), (self.blocks_file_sink_8_0, 0))
        self.connect((self.digital_header_payload_demux_0_0, 0), (self.fft_vxx_0_0, 0))
        self.connect((self.digital_ofdm_chanest_vcvc_0, 0), (self.digital_ofdm_frame_equalizer_vcvc_0, 0))
        self.connect((self.digital_ofdm_chanest_vcvc_0_0, 0), (self.digital_ofdm_frame_equalizer_vcvc_0_0, 0))
        self.connect((self.digital_ofdm_frame_equalizer_vcvc_0, 0), (self.digital_ofdm_serializer_vcc_header, 0))
        self.connect((self.digital_ofdm_frame_equalizer_vcvc_0_0, 0), (self.digital_ofdm_serializer_vcc_header_0, 0))
        self.connect((self.digital_ofdm_serializer_vcc_header, 0), (self.digital_constellation_decoder_cb_0, 0))
        self.connect((self.digital_ofdm_serializer_vcc_header_0, 0), (self.digital_constellation_decoder_cb_0_0, 0))
        self.connect((self.digital_ofdm_sync_sc_cfb_0, 0), (self.analog_frequency_modulator_fc_0, 0))
        self.connect((self.digital_ofdm_sync_sc_cfb_0, 1), (self.digital_header_payload_demux_0, 1))
        self.connect((self.digital_ofdm_sync_sc_cfb_0_0, 0), (self.analog_frequency_modulator_fc_0_0, 0))
        self.connect((self.digital_ofdm_sync_sc_cfb_0_0, 1), (self.digital_header_payload_demux_0_0, 1))
        self.connect((self.fft_vxx_0, 0), (self.digital_ofdm_chanest_vcvc_0, 0))
        self.connect((self.fft_vxx_0_0, 0), (self.digital_ofdm_chanest_vcvc_0_0, 0))
        self.connect((self.uhd_usrp_source_1_0, 0), (self.blocks_delay_0, 0))
        self.connect((self.uhd_usrp_source_1_0, 1), (self.blocks_delay_0_0, 0))
        self.connect((self.uhd_usrp_source_1_0, 1), (self.blocks_file_sink_1_0, 0))
        self.connect((self.uhd_usrp_source_1_0, 0), (self.blocks_file_sink_1_0_0, 0))
        self.connect((self.uhd_usrp_source_1_0, 0), (self.digital_ofdm_sync_sc_cfb_0, 0))
        self.connect((self.uhd_usrp_source_1_0, 1), (self.digital_ofdm_sync_sc_cfb_0_0, 0))
        self.connect((self.uhd_usrp_source_1_0, 0), (self.qtgui_sink_x_0_0, 0))
        self.connect((self.uhd_usrp_source_1_0, 1), (self.qtgui_sink_x_0_1, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "ghostbuster")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_pilot_symbols(self):
        return self.pilot_symbols

    def set_pilot_symbols(self, pilot_symbols):
        self.pilot_symbols = pilot_symbols
        self.set_header_equalizer(digital.ofdm_equalizer_simpledfe(self.fft_len, header_mod.base(), self.occupied_carriers, self.pilot_carriers, self.pilot_symbols))
        self.set_payload_equalizer(digital.ofdm_equalizer_simpledfe(self.fft_len, payload_mod.base(), self.occupied_carriers, self.pilot_carriers, self.pilot_symbols, 1))

    def get_pilot_carriers(self):
        return self.pilot_carriers

    def set_pilot_carriers(self, pilot_carriers):
        self.pilot_carriers = pilot_carriers
        self.set_header_equalizer(digital.ofdm_equalizer_simpledfe(self.fft_len, header_mod.base(), self.occupied_carriers, self.pilot_carriers, self.pilot_symbols))
        self.set_payload_equalizer(digital.ofdm_equalizer_simpledfe(self.fft_len, payload_mod.base(), self.occupied_carriers, self.pilot_carriers, self.pilot_symbols, 1))

    def get_payload_mod(self):
        return self.payload_mod

    def set_payload_mod(self, payload_mod):
        self.payload_mod = payload_mod

    def get_packet_length_tag_key(self):
        return self.packet_length_tag_key

    def set_packet_length_tag_key(self, packet_length_tag_key):
        self.packet_length_tag_key = packet_length_tag_key
        self.set_header_formatter(digital.packet_header_ofdm(self.occupied_carriers, n_syms=1, len_tag_key=self.packet_length_tag_key, frame_len_tag_key=self.length_tag_key, bits_per_header_sym=header_mod.bits_per_symbol(), bits_per_payload_sym=payload_mod.bits_per_symbol(), scramble_header=False))

    def get_occupied_carriers(self):
        return self.occupied_carriers

    def set_occupied_carriers(self, occupied_carriers):
        self.occupied_carriers = occupied_carriers
        self.set_header_equalizer(digital.ofdm_equalizer_simpledfe(self.fft_len, header_mod.base(), self.occupied_carriers, self.pilot_carriers, self.pilot_symbols))
        self.set_header_formatter(digital.packet_header_ofdm(self.occupied_carriers, n_syms=1, len_tag_key=self.packet_length_tag_key, frame_len_tag_key=self.length_tag_key, bits_per_header_sym=header_mod.bits_per_symbol(), bits_per_payload_sym=payload_mod.bits_per_symbol(), scramble_header=False))
        self.set_payload_equalizer(digital.ofdm_equalizer_simpledfe(self.fft_len, payload_mod.base(), self.occupied_carriers, self.pilot_carriers, self.pilot_symbols, 1))

    def get_length_tag_key(self):
        return self.length_tag_key

    def set_length_tag_key(self, length_tag_key):
        self.length_tag_key = length_tag_key
        self.set_header_formatter(digital.packet_header_ofdm(self.occupied_carriers, n_syms=1, len_tag_key=self.packet_length_tag_key, frame_len_tag_key=self.length_tag_key, bits_per_header_sym=header_mod.bits_per_symbol(), bits_per_payload_sym=payload_mod.bits_per_symbol(), scramble_header=False))

    def get_header_mod(self):
        return self.header_mod

    def set_header_mod(self, header_mod):
        self.header_mod = header_mod

    def get_fft_len(self):
        return self.fft_len

    def set_fft_len(self, fft_len):
        self.fft_len = fft_len
        self.set_header_equalizer(digital.ofdm_equalizer_simpledfe(self.fft_len, header_mod.base(), self.occupied_carriers, self.pilot_carriers, self.pilot_symbols))
        self.set_payload_equalizer(digital.ofdm_equalizer_simpledfe(self.fft_len, payload_mod.base(), self.occupied_carriers, self.pilot_carriers, self.pilot_symbols, 1))
        self.analog_frequency_modulator_fc_0.set_sensitivity(-2.0/self.fft_len)
        self.analog_frequency_modulator_fc_0_0.set_sensitivity(-2.0/self.fft_len)
        self.blocks_delay_0.set_dly(self.fft_len+self.fft_len//4)
        self.blocks_delay_0_0.set_dly(self.fft_len+self.fft_len//4)

    def get_sync_word2(self):
        return self.sync_word2

    def set_sync_word2(self, sync_word2):
        self.sync_word2 = sync_word2

    def get_sync_word1(self):
        return self.sync_word1

    def set_sync_word1(self, sync_word1):
        self.sync_word1 = sync_word1

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.uhd_usrp_source_1_0.set_samp_rate(self.samp_rate)

    def get_payload_equalizer(self):
        return self.payload_equalizer

    def set_payload_equalizer(self, payload_equalizer):
        self.payload_equalizer = payload_equalizer

    def get_packet_len(self):
        return self.packet_len

    def set_packet_len(self, packet_len):
        self.packet_len = packet_len

    def get_header_formatter(self):
        return self.header_formatter

    def set_header_formatter(self, header_formatter):
        self.header_formatter = header_formatter

    def get_header_equalizer(self):
        return self.header_equalizer

    def set_header_equalizer(self, header_equalizer):
        self.header_equalizer = header_equalizer

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.qtgui_sink_x_0_0.set_frequency_range(self.freq, self.band_width)
        self.qtgui_sink_x_0_1.set_frequency_range(self.freq, self.band_width)
        self.uhd_usrp_source_1_0.set_center_freq(self.freq, 0)
        self.uhd_usrp_source_1_0.set_center_freq(self.freq, 1)

    def get_band_width(self):
        return self.band_width

    def set_band_width(self, band_width):
        self.band_width = band_width
        self.qtgui_sink_x_0_0.set_frequency_range(self.freq, self.band_width)
        self.qtgui_sink_x_0_1.set_frequency_range(self.freq, self.band_width)
        self.uhd_usrp_source_1_0.set_bandwidth(self.band_width, 0)
        self.uhd_usrp_source_1_0.set_bandwidth(self.band_width, 1)




def main(top_block_cls=ghostbuster, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
