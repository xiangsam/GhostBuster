options:
  parameters:
    author: ''
    catch_exceptions: 'True'
    category: Custom
    cmake_opt: ''
    comment: ''
    copyright: ''
    description: wireless
    gen_cmake: 'On'
    gen_linking: dynamic
    generate_options: qt_gui
    hier_block_src_path: '.:'
    id: ghostbuster
    max_nouts: '0'
    output_language: python
    placement: (0,0)
    qt_qss_theme: ''
    realtime_scheduling: ''
    run: 'True'
    run_command: '{python} -u {filename}'
    run_options: prompt
    sizing_mode: fixed
    thread_safe_setters: ''
    title: ghostbuster
    window_size: (1000,1000)
  states:
    bus_sink: false
    bus_source: false
    bus_structure: null
    coordinate: [0, -1]
    rotation: 0
    state: enabled

blocks:
- name: band_width
  id: variable
  parameters:
    comment: ''
    value: 6e6
  states:
    bus_sink: false
    bus_source: false
    bus_structure: null
    coordinate: [1288, 68.0]
    rotation: 0
    state: true
- name: fft_len
  id: variable
  parameters:
    comment: ''
    value: '64'
  states:
    bus_sink: false
    bus_source: false
    bus_structure: null
    coordinate: [301, -1]
    rotation: 0
    state: enabled
- name: freq
  id: variable
  parameters:
    comment: ''
    value: 5.08e9
  states:
    bus_sink: false
    bus_source: false
    bus_structure: null
    coordinate: [1296, 0.0]
    rotation: 0
    state: true
- name: header_equalizer
  id: variable
  parameters:
    comment: ''
    value: digital.ofdm_equalizer_simpledfe(fft_len, header_mod.base(), occupied_carriers,
      pilot_carriers, pilot_symbols)
  states:
    bus_sink: false
    bus_source: false
    bus_structure: null
    coordinate: [931, 69]
    rotation: 0
    state: enabled
- name: header_formatter
  id: variable
  parameters:
    comment: ''
    value: digital.packet_header_ofdm(occupied_carriers, n_syms=1, len_tag_key=packet_length_tag_key,
      frame_len_tag_key=length_tag_key, bits_per_header_sym=header_mod.bits_per_symbol(),
      bits_per_payload_sym=payload_mod.bits_per_symbol(), scramble_header=False)
  states:
    bus_sink: false
    bus_source: false
    bus_structure: null
    coordinate: [855, 0]
    rotation: 0
    state: enabled
- name: header_mod
  id: variable
  parameters:
    comment: ''
    value: digital.constellation_bpsk()
  states:
    bus_sink: false
    bus_source: false
    bus_structure: null
    coordinate: [490, 0]
    rotation: 0
    state: enabled
- name: length_tag_key
  id: variable
  parameters:
    comment: ''
    value: '"frame_len"'
  states:
    bus_sink: false
    bus_source: false
    bus_structure: null
    coordinate: [376, 0.0]
    rotation: 0
    state: enabled
- name: occupied_carriers
  id: variable
  parameters:
    comment: ''
    value: ([-26, -25, -24, -23, -22, -20, -19, -18, -17, -16, -15, -14, -13, -12,
      -11, -10, -9, -8, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12,
      13, 14, 15, 16, 17, 18, 19, 20, 22, 23, 24, 25, 26],)
  states:
    bus_sink: false
    bus_source: false
    bus_structure: null
    coordinate: [541, 70]
    rotation: 0
    state: enabled
- name: packet_len
  id: variable
  parameters:
    comment: ''
    value: '96'
  states:
    bus_sink: false
    bus_source: false
    bus_structure: null
    coordinate: [1504, 0.0]
    rotation: 0
    state: true
- name: packet_length_tag_key
  id: variable
  parameters:
    comment: ''
    value: '"packet_len"'
  states:
    bus_sink: false
    bus_source: false
    bus_structure: null
    coordinate: [1132, 0]
    rotation: 0
    state: enabled
- name: payload_equalizer
  id: variable
  parameters:
    comment: ''
    value: digital.ofdm_equalizer_simpledfe(fft_len, payload_mod.base(), occupied_carriers,
      pilot_carriers, pilot_symbols, 1)
  states:
    bus_sink: false
    bus_source: false
    bus_structure: null
    coordinate: [1112, 73]
    rotation: 0
    state: enabled
- name: payload_mod
  id: variable
  parameters:
    comment: ''
    value: digital.constellation_qpsk()
  states:
    bus_sink: false
    bus_source: false
    bus_structure: null
    coordinate: [663, 1]
    rotation: 0
    state: enabled
- name: pilot_carriers
  id: variable
  parameters:
    comment: ''
    value: ((-21, -7, 7, 21,),)
  states:
    bus_sink: false
    bus_source: false
    bus_structure: null
    coordinate: [692, 70]
    rotation: 0
    state: enabled
- name: pilot_symbols
  id: variable
  parameters:
    comment: ''
    value: ((1, 1, 1, -1,),)
  states:
    bus_sink: false
    bus_source: false
    bus_structure: null
    coordinate: [813, 70]
    rotation: 0
    state: enabled
- name: samp_rate
  id: variable
  parameters:
    comment: ''
    value: '2000000'
  states:
    bus_sink: false
    bus_source: false
    bus_structure: null
    coordinate: [1392, 4.0]
    rotation: 0
    state: enabled
- name: sync_word1
  id: variable
  parameters:
    comment: ''
    value: '[0., 0., 0., 0., 0., 0., 0., 1.41421356, 0., -1.41421356, 0., 1.41421356,
      0., -1.41421356, 0., -1.41421356, 0., -1.41421356, 0., 1.41421356, 0., -1.41421356,
      0., 1.41421356, 0., -1.41421356, 0., -1.41421356, 0., -1.41421356, 0., -1.41421356,
      0., 1.41421356, 0., -1.41421356, 0., 1.41421356, 0., 1.41421356, 0., 1.41421356,
      0., -1.41421356, 0., 1.41421356, 0., 1.41421356, 0., 1.41421356, 0., -1.41421356,
      0., 1.41421356, 0., 1.41421356, 0., 1.41421356, 0., 0., 0., 0., 0., 0.]'
  states:
    bus_sink: false
    bus_source: false
    bus_structure: null
    coordinate: [272, 72.0]
    rotation: 0
    state: enabled
- name: sync_word2
  id: variable
  parameters:
    comment: ''
    value: '[0j, 0j, 0j, 0j, 0j, 0j, (-1+0j), (-1+0j), (-1+0j), (-1+0j), (1+0j), (1+0j),
      (-1+0j), (-1+0j), (-1+0j), (1+0j), (-1+0j), (1+0j), (1+0j), (1 +0j), (1+0j),
      (1+0j), (-1+0j), (-1+0j), (-1+0j), (-1+0j), (-1+0j), (1+0j), (-1+0j), (-1+0j),
      (1+0j), (-1+0j), 0j, (1+0j), (-1+0j), (1+0j), (1+0j), (1+0j), (-1+0j), (1+0j),
      (1+0j), (1+0j), (-1+0j), (1+0j), (1+0j), (1+0j), (1+0j), (-1+0j), (1+0j), (-1+0j),
      (-1+0j), (-1+0j), (1+0j), (-1+0j), (1+0j), (-1+0j), (-1+0j), (-1+0j), (-1+0j),
      0j, 0j, 0j, 0j, 0j]'
  states:
    bus_sink: false
    bus_source: false
    bus_structure: null
    coordinate: [400, 72.0]
    rotation: 0
    state: enabled
- name: analog_frequency_modulator_fc_0
  id: analog_frequency_modulator_fc
  parameters:
    affinity: ''
    alias: ''
    comment: "\u6D88\u9664\u5C0F\u6570\u500D\u9891\u504F"
    maxoutbuf: '0'
    minoutbuf: '0'
    sensitivity: -2.0/fft_len
  states:
    bus_sink: false
    bus_source: false
    bus_structure: null
    coordinate: [880, 180.0]
    rotation: 0
    state: enabled
- name: analog_frequency_modulator_fc_0_0
  id: analog_frequency_modulator_fc
  parameters:
    affinity: ''
    alias: ''
    comment: "\u6D88\u9664\u5C0F\u6570\u500D\u9891\u504F"
    maxoutbuf: '0'
    minoutbuf: '0'
    sensitivity: -2.0/fft_len
  states:
    bus_sink: false
    bus_source: false
    bus_structure: null
    coordinate: [480, 1104.0]
    rotation: 0
    state: enabled
- name: blocks_delay_0
  id: blocks_delay
  parameters:
    affinity: ''
    alias: ''
    comment: "\u5EF6\u8FDF\u4E00\u4E2AOFDM symbol(\u542BCP)"
    delay: fft_len+fft_len//4
    maxoutbuf: '0'
    minoutbuf: '0'
    num_ports: '1'
    type: complex
    vlen: '1'
  states:
    bus_sink: false
    bus_source: false
    bus_structure: null
    coordinate: [648, 344.0]
    rotation: 0
    state: enabled
- name: blocks_delay_0_0
  id: blocks_delay
  parameters:
    affinity: ''
    alias: ''
    comment: "\u5EF6\u8FDF\u4E00\u4E2AOFDM symbol(\u542BCP)"
    delay: fft_len+fft_len//4
    maxoutbuf: '0'
    minoutbuf: '0'
    num_ports: '1'
    type: complex
    vlen: '1'
  states:
    bus_sink: false
    bus_source: false
    bus_structure: null
    coordinate: [320, 1168.0]
    rotation: 0
    state: enabled
- name: blocks_file_meta_sink_0
  id: blocks_file_meta_sink
  parameters:
    affinity: ''
    alias: ''
    comment: ''
    detached: 'False'
    extra_dict: pmt.make_dict()
    file: /home/samrito/workarea/OFDM0516/0520_seperate/test
    max_seg_size: '1000000'
    rel_rate: '1'
    samp_rate: samp_rate
    type: complex
    unbuffered: 'False'
    vlen: '1'
  states:
    bus_sink: false
    bus_source: false
    bus_structure: null
    coordinate: [432, 540.0]
    rotation: 0
    state: disabled
- name: blocks_file_sink_0
  id: blocks_file_sink
  parameters:
    affinity: ''
    alias: ''
    append: 'False'
    comment: ''
    file: /home/samrito/workarea/OFDM0516/0520_seperate/beforeDemuxAA
    type: complex
    unbuffered: 'False'
    vlen: '1'
  states:
    bus_sink: false
    bus_source: false
    bus_structure: null
    coordinate: [1344, 188.0]
    rotation: 0
    state: enabled
- name: blocks_file_sink_0_0
  id: blocks_file_sink
  parameters:
    affinity: ''
    alias: ''
    append: 'False'
    comment: ''
    file: /home/samrito/workarea/OFDM0516/0520_seperate/beforeDemuxAB
    type: complex
    unbuffered: 'False'
    vlen: '1'
  states:
    bus_sink: false
    bus_source: false
    bus_structure: null
    coordinate: [824, 1132.0]
    rotation: 0
    state: enabled
- name: blocks_file_sink_1
  id: blocks_file_sink
  parameters:
    affinity: ''
    alias: ''
    append: 'False'
    comment: ''
    file: /home/samrito/workarea/OFDM0516/0520_seperate/freq
    type: float
    unbuffered: 'False'
    vlen: '1'
  states:
    bus_sink: false
    bus_source: false
    bus_structure: null
    coordinate: [616, 148.0]
    rotation: 0
    state: disabled
- name: blocks_file_sink_14
  id: blocks_file_sink
  parameters:
    affinity: ''
    alias: ''
    append: 'False'
    comment: ''
    file: /home/samrito/workarea/OFDM0516/0520_seperate/tag_dataAA
    type: byte
    unbuffered: 'False'
    vlen: '1'
  states:
    bus_sink: false
    bus_source: false
    bus_structure: null
    coordinate: [1584, 972.0]
    rotation: 0
    state: disabled
- name: blocks_file_sink_14_0
  id: blocks_file_sink
  parameters:
    affinity: ''
    alias: ''
    append: 'False'
    comment: ''
    file: /home/samrito/workarea/OFDM0516/0520_seperate/tag_dataAB
    type: byte
    unbuffered: 'False'
    vlen: '1'
  states:
    bus_sink: false
    bus_source: false
    bus_structure: null
    coordinate: [1000, 1956.0]
    rotation: 0
    state: disabled
- name: blocks_file_sink_1_0
  id: blocks_file_sink
  parameters:
    affinity: ''
    alias: ''
    append: 'False'
    comment: ''
    file: /home/samrito/workarea/OFDM0516/0520_seperate/afterChannelAB
    type: complex
    unbuffered: 'False'
    vlen: '1'
  states:
    bus_sink: false
    bus_source: false
    bus_structure: null
    coordinate: [400, 668.0]
    rotation: 0
    state: enabled
- name: blocks_file_sink_1_0_0
  id: blocks_file_sink
  parameters:
    affinity: ''
    alias: ''
    append: 'False'
    comment: ''
    file: /home/samrito/workarea/OFDM0516/0520_seperate/afterChannelAA
    type: complex
    unbuffered: 'False'
    vlen: '1'
  states:
    bus_sink: false
    bus_source: false
    bus_structure: null
    coordinate: [400, 500.0]
    rotation: 0
    state: enabled
- name: blocks_file_sink_1_1
  id: blocks_file_sink
  parameters:
    affinity: ''
    alias: ''
    append: 'False'
    comment: ''
    file: /home/samrito/workarea/OFDM0516/0520_seperate/detect
    type: byte
    unbuffered: 'False'
    vlen: '1'
  states:
    bus_sink: false
    bus_source: false
    bus_structure: null
    coordinate: [632, 276.0]
    rotation: 0
    state: disabled
- name: blocks_file_sink_8
  id: blocks_file_sink
  parameters:
    affinity: ''
    alias: ''
    append: 'False'
    comment: ''
    file: /home/samrito/workarea/OFDM0516/0520_seperate/payload_streamAA
    type: complex
    unbuffered: 'False'
    vlen: '64'
  states:
    bus_sink: false
    bus_source: false
    bus_structure: null
    coordinate: [800, 716.0]
    rotation: 0
    state: enabled
- name: blocks_file_sink_8_0
  id: blocks_file_sink
  parameters:
    affinity: ''
    alias: ''
    append: 'False'
    comment: ''
    file: /home/samrito/workarea/OFDM0516/0520_seperate/payload_streamAB
    type: complex
    unbuffered: 'False'
    vlen: '64'
  states:
    bus_sink: false
    bus_source: false
    bus_structure: null
    coordinate: [248, 1820.0]
    rotation: 0
    state: enabled
- name: blocks_file_sink_9
  id: blocks_file_sink
  parameters:
    affinity: ''
    alias: ''
    append: 'False'
    comment: ''
    file: /home/samrito/workarea/OFDM0516/0520_seperate/header_streamAA
    type: complex
    unbuffered: 'False'
    vlen: '64'
  states:
    bus_sink: false
    bus_source: false
    bus_structure: null
    coordinate: [912, 468.0]
    rotation: 0
    state: disabled
- name: blocks_file_sink_9_0
  id: blocks_file_sink
  parameters:
    affinity: ''
    alias: ''
    append: 'False'
    comment: ''
    file: /home/samrito/workarea/OFDM0516/0520_seperate/header_streamAB
    type: complex
    unbuffered: 'False'
    vlen: '64'
  states:
    bus_sink: false
    bus_source: false
    bus_structure: null
    coordinate: [232, 1396.0]
    rotation: 0
    state: disabled
- name: blocks_multiply_xx_0
  id: blocks_multiply_xx
  parameters:
    affinity: ''
    alias: ''
    comment: ''
    maxoutbuf: '0'
    minoutbuf: '0'
    num_inputs: '2'
    type: complex
    vlen: '1'
  states:
    bus_sink: false
    bus_source: false
    bus_structure: null
    coordinate: [1088, 184.0]
    rotation: 0
    state: enabled
- name: blocks_multiply_xx_0_0
  id: blocks_multiply_xx
  parameters:
    affinity: ''
    alias: ''
    comment: ''
    maxoutbuf: '0'
    minoutbuf: '0'
    num_inputs: '2'
    type: complex
    vlen: '1'
  states:
    bus_sink: false
    bus_source: false
    bus_structure: null
    coordinate: [656, 1200.0]
    rotation: 0
    state: enabled
- name: blocks_repack_bits_bb_0
  id: blocks_repack_bits_bb
  parameters:
    affinity: ''
    alias: ''
    align_output: 'True'
    comment: ''
    endianness: gr.GR_LSB_FIRST
    k: payload_mod.bits_per_symbol()
    l: '8'
    len_tag_key: packet_length_tag_key
    maxoutbuf: '0'
    minoutbuf: '0'
  states:
    bus_sink: false
    bus_source: false
    bus_structure: null
    coordinate: [1080, 984.0]
    rotation: 0
    state: disabled
- name: blocks_repack_bits_bb_0_0
  id: blocks_repack_bits_bb
  parameters:
    affinity: ''
    alias: ''
    align_output: 'True'
    comment: ''
    endianness: gr.GR_LSB_FIRST
    k: payload_mod.bits_per_symbol()
    l: '8'
    len_tag_key: packet_length_tag_key
    maxoutbuf: '0'
    minoutbuf: '0'
  states:
    bus_sink: false
    bus_source: false
    bus_structure: null
    coordinate: [496, 1960.0]
    rotation: 0
    state: disabled
- name: blocks_throttle_0
  id: blocks_throttle
  parameters:
    affinity: ''
    alias: ''
    comment: ''
    ignoretag: 'True'
    maxoutbuf: '0'
    minoutbuf: '0'
    samples_per_second: 10k
    type: complex
    vlen: '1'
  states:
    bus_sink: false
    bus_source: false
    bus_structure: null
    coordinate: [408, 272.0]
    rotation: 0
    state: disabled
- name: blocks_throttle_1
  id: blocks_throttle
  parameters:
    affinity: ''
    alias: ''
    comment: ''
    ignoretag: 'True'
    maxoutbuf: '0'
    minoutbuf: '0'
    samples_per_second: 10k
    type: complex
    vlen: '1'
  states:
    bus_sink: false
    bus_source: false
    bus_structure: null
    coordinate: [320, 1008.0]
    rotation: 0
    state: disabled
- name: digital_constellation_decoder_cb_0
  id: digital_constellation_decoder_cb
  parameters:
    affinity: ''
    alias: ''
    comment: "\u89E3\u7B26\u53F7\u6620\u5C04"
    constellation: header_mod.base()
    maxoutbuf: '0'
    minoutbuf: '0'
  states:
    bus_sink: false
    bus_source: false
    bus_structure: null
    coordinate: [1624, 504.0]
    rotation: 180
    state: enabled
- name: digital_constellation_decoder_cb_0_0
  id: digital_constellation_decoder_cb
  parameters:
    affinity: ''
    alias: ''
    comment: "\u89E3\u7B26\u53F7\u6620\u5C04"
    constellation: header_mod.base()
    maxoutbuf: '0'
    minoutbuf: '0'
  states:
    bus_sink: false
    bus_source: false
    bus_structure: null
    coordinate: [1104, 1408.0]
    rotation: 180
    state: enabled
- name: digital_constellation_decoder_cb_1
  id: digital_constellation_decoder_cb
  parameters:
    affinity: ''
    alias: ''
    comment: ''
    constellation: payload_mod.base()
    maxoutbuf: '0'
    minoutbuf: '0'
  states:
    bus_sink: false
    bus_source: false
    bus_structure: null
    coordinate: [824, 992.0]
    rotation: 0
    state: disabled
- name: digital_constellation_decoder_cb_1_0
  id: digital_constellation_decoder_cb
  parameters:
    affinity: ''
    alias: ''
    comment: ''
    constellation: payload_mod.base()
    maxoutbuf: '0'
    minoutbuf: '0'
  states:
    bus_sink: false
    bus_source: false
    bus_structure: null
    coordinate: [240, 1968.0]
    rotation: 0
    state: disabled
- name: digital_crc32_bb_0
  id: digital_crc32_bb
  parameters:
    affinity: ''
    alias: ''
    check: 'True'
    comment: ''
    lengthtagname: packet_length_tag_key
    maxoutbuf: '0'
    minoutbuf: '0'
    packed: 'True'
  states:
    bus_sink: false
    bus_source: false
    bus_structure: null
    coordinate: [1312, 972.0]
    rotation: 0
    state: disabled
- name: digital_crc32_bb_0_0
  id: digital_crc32_bb
  parameters:
    affinity: ''
    alias: ''
    check: 'True'
    comment: ''
    lengthtagname: packet_length_tag_key
    maxoutbuf: '0'
    minoutbuf: '0'
    packed: 'True'
  states:
    bus_sink: false
    bus_source: false
    bus_structure: null
    coordinate: [720, 1956.0]
    rotation: 0
    state: disabled
- name: digital_header_payload_demux_0
  id: digital_header_payload_demux
  parameters:
    affinity: ''
    alias: ''
    comment: ''
    guard_interval: fft_len//4
    header_len: '3'
    header_padding: '0'
    items_per_symbol: fft_len
    length_tag_key: length_tag_key
    maxoutbuf: '0'
    minoutbuf: '0'
    output_symbols: 'True'
    samp_rate: samp_rate
    special_tags: ()
    timing_tag_key: '"rx_time"'
    trigger_tag_key: '""'
    type: complex
  states:
    bus_sink: false
    bus_source: false
    bus_structure: null
    coordinate: [1312, 296.0]
    rotation: 0
    state: enabled
- name: digital_header_payload_demux_0_0
  id: digital_header_payload_demux
  parameters:
    affinity: ''
    alias: ''
    comment: ''
    guard_interval: fft_len//4
    header_len: '3'
    header_padding: '0'
    items_per_symbol: fft_len
    length_tag_key: length_tag_key
    maxoutbuf: '0'
    minoutbuf: '0'
    output_symbols: 'True'
    samp_rate: samp_rate
    special_tags: ()
    timing_tag_key: '"rx_time"'
    trigger_tag_key: '""'
    type: complex
  states:
    bus_sink: false
    bus_source: false
    bus_structure: null
    coordinate: [992, 1192.0]
    rotation: 0
    state: enabled
- name: digital_ofdm_chanest_vcvc_0
  id: digital_ofdm_chanest_vcvc
  parameters:
    affinity: ''
    alias: ''
    comment: ''
    eq_noise_red_len: '0'
    force_one_symbol: 'False'
    max_carr_offset: '3'
    maxoutbuf: '0'
    minoutbuf: '0'
    n_data_symbols: '1'
    sync_symbol1: sync_word1
    sync_symbol2: sync_word2
  states:
    bus_sink: false
    bus_source: false
    bus_structure: null
    coordinate: [1112, 596.0]
    rotation: 0
    state: enabled
- name: digital_ofdm_chanest_vcvc_0_0
  id: digital_ofdm_chanest_vcvc
  parameters:
    affinity: ''
    alias: ''
    comment: ''
    eq_noise_red_len: '0'
    force_one_symbol: 'False'
    max_carr_offset: '3'
    maxoutbuf: '0'
    minoutbuf: '0'
    n_data_symbols: '1'
    sync_symbol1: sync_word1
    sync_symbol2: sync_word2
  states:
    bus_sink: false
    bus_source: false
    bus_structure: null
    coordinate: [504, 1548.0]
    rotation: 0
    state: enabled
- name: digital_ofdm_frame_equalizer_vcvc_0
  id: digital_ofdm_frame_equalizer_vcvc
  parameters:
    affinity: ''
    alias: ''
    comment: "\u7EA0\u6B63\u6574\u6570\u500D\u9891\u504F\uFF0C\u5BF9\u63A5\u6536\u4FE1\
      \u53F7\u8FDB\u884C\u5747\u8861"
    cp_len: fft_len//4
    equalizer: header_equalizer.base()
    fft_len: fft_len
    fixed_frame_len: '1'
    len_tag_key: length_tag_key
    maxoutbuf: '0'
    minoutbuf: '0'
    propagate_channel_state: 'True'
  states:
    bus_sink: false
    bus_source: false
    bus_structure: null
    coordinate: [1424, 588.0]
    rotation: 0
    state: enabled
- name: digital_ofdm_frame_equalizer_vcvc_0_0
  id: digital_ofdm_frame_equalizer_vcvc
  parameters:
    affinity: ''
    alias: ''
    comment: "\u7EA0\u6B63\u6574\u6570\u500D\u9891\u504F\uFF0C\u5BF9\u63A5\u6536\u4FE1\
      \u53F7\u8FDB\u884C\u5747\u8861"
    cp_len: fft_len//4
    equalizer: header_equalizer.base()
    fft_len: fft_len
    fixed_frame_len: '1'
    len_tag_key: length_tag_key
    maxoutbuf: '0'
    minoutbuf: '0'
    propagate_channel_state: 'True'
  states:
    bus_sink: false
    bus_source: false
    bus_structure: null
    coordinate: [808, 1540.0]
    rotation: 0
    state: enabled
- name: digital_ofdm_frame_equalizer_vcvc_1
  id: digital_ofdm_frame_equalizer_vcvc
  parameters:
    affinity: ''
    alias: ''
    comment: ''
    cp_len: fft_len//4
    equalizer: payload_equalizer.base()
    fft_len: fft_len
    fixed_frame_len: '0'
    len_tag_key: length_tag_key
    maxoutbuf: '0'
    minoutbuf: '0'
    propagate_channel_state: 'True'
  states:
    bus_sink: false
    bus_source: false
    bus_structure: null
    coordinate: [1200, 804.0]
    rotation: 0
    state: disabled
- name: digital_ofdm_frame_equalizer_vcvc_1_0
  id: digital_ofdm_frame_equalizer_vcvc
  parameters:
    affinity: ''
    alias: ''
    comment: ''
    cp_len: fft_len//4
    equalizer: payload_equalizer.base()
    fft_len: fft_len
    fixed_frame_len: '0'
    len_tag_key: length_tag_key
    maxoutbuf: '0'
    minoutbuf: '0'
    propagate_channel_state: 'True'
  states:
    bus_sink: false
    bus_source: false
    bus_structure: null
    coordinate: [616, 1780.0]
    rotation: 0
    state: disabled
- name: digital_ofdm_serializer_vcc_header
  id: digital_ofdm_serializer_vcc
  parameters:
    affinity: ''
    alias: ''
    carr_offset_key: ''
    comment: "\u4F59\u4E0Bdata subcarrier"
    fft_len: fft_len
    input_is_shifted: 'True'
    len_tag_key: length_tag_key
    maxoutbuf: '0'
    minoutbuf: '0'
    occupied_carriers: occupied_carriers
    packet_len_tag_key: ''
    symbols_skipped: '0'
  states:
    bus_sink: false
    bus_source: false
    bus_structure: null
    coordinate: [1640, 612.0]
    rotation: 0
    state: enabled
- name: digital_ofdm_serializer_vcc_header_0
  id: digital_ofdm_serializer_vcc
  parameters:
    affinity: ''
    alias: ''
    carr_offset_key: ''
    comment: "\u4F59\u4E0Bdata subcarrier"
    fft_len: fft_len
    input_is_shifted: 'True'
    len_tag_key: length_tag_key
    maxoutbuf: '0'
    minoutbuf: '0'
    occupied_carriers: occupied_carriers
    packet_len_tag_key: ''
    symbols_skipped: '0'
  states:
    bus_sink: false
    bus_source: false
    bus_structure: null
    coordinate: [1088, 1564.0]
    rotation: 0
    state: enabled
- name: digital_ofdm_serializer_vcc_payload
  id: digital_ofdm_serializer_vcc
  parameters:
    affinity: ''
    alias: ''
    carr_offset_key: ''
    comment: ''
    fft_len: fft_len
    input_is_shifted: 'True'
    len_tag_key: length_tag_key
    maxoutbuf: '0'
    minoutbuf: '0'
    occupied_carriers: occupied_carriers
    packet_len_tag_key: packet_length_tag_key
    symbols_skipped: '1'
  states:
    bus_sink: false
    bus_source: false
    bus_structure: null
    coordinate: [1600, 804.0]
    rotation: 0
    state: disabled
- name: digital_ofdm_serializer_vcc_payload_0
  id: digital_ofdm_serializer_vcc
  parameters:
    affinity: ''
    alias: ''
    carr_offset_key: ''
    comment: ''
    fft_len: fft_len
    input_is_shifted: 'True'
    len_tag_key: length_tag_key
    maxoutbuf: '0'
    minoutbuf: '0'
    occupied_carriers: occupied_carriers
    packet_len_tag_key: packet_length_tag_key
    symbols_skipped: '1'
  states:
    bus_sink: false
    bus_source: false
    bus_structure: null
    coordinate: [1016, 1780.0]
    rotation: 0
    state: disabled
- name: digital_ofdm_sync_sc_cfb_0
  id: digital_ofdm_sync_sc_cfb
  parameters:
    affinity: ''
    alias: ''
    comment: "\u7B26\u53F7\u5B9A\u65F6\u540C\u6B65\uFF0C\u53BB\u9664\u5C0F\u6570\u90E8\
      \u5206\u7684\u8F7D\u6CE2\u9891\u504F"
    cp_len: fft_len//4
    fft_len: fft_len
    maxoutbuf: '0'
    minoutbuf: '0'
    threshold: '0.9'
    use_even_carriers: 'False'
  states:
    bus_sink: false
    bus_source: false
    bus_structure: null
    coordinate: [320, 196.0]
    rotation: 0
    state: enabled
- name: digital_ofdm_sync_sc_cfb_0_0
  id: digital_ofdm_sync_sc_cfb
  parameters:
    affinity: ''
    alias: ''
    comment: "\u7B26\u53F7\u5B9A\u65F6\u540C\u6B65\uFF0C\u53BB\u9664\u5C0F\u6570\u90E8\
      \u5206\u7684\u8F7D\u6CE2\u9891\u504F"
    cp_len: fft_len//4
    fft_len: fft_len
    maxoutbuf: '0'
    minoutbuf: '0'
    threshold: '0.9'
    use_even_carriers: 'False'
  states:
    bus_sink: false
    bus_source: false
    bus_structure: null
    coordinate: [336, 916.0]
    rotation: 0
    state: enabled
- name: digital_packet_headerparser_b_0
  id: digital_packet_headerparser_b
  parameters:
    affinity: ''
    alias: ''
    comment: "\u89E3\u5E27\u5934\u4FE1\u606F"
    header_formatter: header_formatter.base()
    maxoutbuf: '0'
    minoutbuf: '0'
  states:
    bus_sink: false
    bus_source: false
    bus_structure: null
    coordinate: [1360, 504.0]
    rotation: 180
    state: enabled
- name: digital_packet_headerparser_b_0_0
  id: digital_packet_headerparser_b
  parameters:
    affinity: ''
    alias: ''
    comment: "\u89E3\u5E27\u5934\u4FE1\u606F"
    header_formatter: header_formatter.base()
    maxoutbuf: '0'
    minoutbuf: '0'
  states:
    bus_sink: false
    bus_source: false
    bus_structure: null
    coordinate: [832, 1408.0]
    rotation: 180
    state: enabled
- name: fft_vxx_0
  id: fft_vxx
  parameters:
    affinity: ''
    alias: ''
    comment: ''
    fft_size: fft_len
    forward: 'True'
    maxoutbuf: '0'
    minoutbuf: '0'
    nthreads: '1'
    shift: 'True'
    type: complex
    window: ()
  states:
    bus_sink: false
    bus_source: false
    bus_structure: null
    coordinate: [816, 588.0]
    rotation: 0
    state: enabled
- name: fft_vxx_0_0
  id: fft_vxx
  parameters:
    affinity: ''
    alias: ''
    comment: ''
    fft_size: fft_len
    forward: 'True'
    maxoutbuf: '0'
    minoutbuf: '0'
    nthreads: '1'
    shift: 'True'
    type: complex
    window: ()
  states:
    bus_sink: false
    bus_source: false
    bus_structure: null
    coordinate: [280, 1548.0]
    rotation: 0
    state: enabled
- name: fft_vxx_1
  id: fft_vxx
  parameters:
    affinity: ''
    alias: ''
    comment: ''
    fft_size: fft_len
    forward: 'True'
    maxoutbuf: '0'
    minoutbuf: '0'
    nthreads: '1'
    shift: 'True'
    type: complex
    window: ()
  states:
    bus_sink: false
    bus_source: false
    bus_structure: null
    coordinate: [896, 804.0]
    rotation: 0
    state: disabled
- name: fft_vxx_1_0
  id: fft_vxx
  parameters:
    affinity: ''
    alias: ''
    comment: ''
    fft_size: fft_len
    forward: 'True'
    maxoutbuf: '0'
    minoutbuf: '0'
    nthreads: '1'
    shift: 'True'
    type: complex
    window: ()
  states:
    bus_sink: false
    bus_source: false
    bus_structure: null
    coordinate: [312, 1780.0]
    rotation: 0
    state: disabled
- name: import_0
  id: import
  parameters:
    alias: ''
    comment: ''
    imports: import pmt
  states:
    bus_sink: false
    bus_source: false
    bus_structure: null
    coordinate: [168, 60.0]
    rotation: 0
    state: true
- name: import_1
  id: import
  parameters:
    alias: ''
    comment: ''
    imports: from gnuradio.digital.utils import tagged_streams
  states:
    bus_sink: false
    bus_source: false
    bus_structure: null
    coordinate: [160, 4.0]
    rotation: 0
    state: enabled
- name: network_tcp_source_0
  id: network_tcp_source
  parameters:
    addr: 127.0.0.1
    affinity: ''
    alias: ''
    comment: ''
    maxoutbuf: '0'
    minoutbuf: '0'
    port: '2000'
    server: 'True'
    type: complex
    vlen: '1'
  states:
    bus_sink: false
    bus_source: false
    bus_structure: null
    coordinate: [104, 180.0]
    rotation: 0
    state: disabled
- name: qtgui_sink_x_0_0
  id: qtgui_sink_x
  parameters:
    affinity: ''
    alias: ''
    bw: band_width
    comment: ''
    fc: freq
    fftsize: '1024'
    gui_hint: ''
    maxoutbuf: '0'
    minoutbuf: '0'
    name: '""'
    plotconst: 'True'
    plotfreq: 'True'
    plottime: 'True'
    plotwaterfall: 'True'
    rate: '10'
    showports: 'False'
    showrf: 'False'
    type: complex
    wintype: window.WIN_BLACKMAN_hARRIS
  states:
    bus_sink: false
    bus_source: false
    bus_structure: null
    coordinate: [336, 372.0]
    rotation: 0
    state: enabled
- name: qtgui_sink_x_0_1
  id: qtgui_sink_x
  parameters:
    affinity: ''
    alias: ''
    bw: band_width
    comment: ''
    fc: freq
    fftsize: '1024'
    gui_hint: ''
    maxoutbuf: '0'
    minoutbuf: '0'
    name: '""'
    plotconst: 'True'
    plotfreq: 'True'
    plottime: 'True'
    plotwaterfall: 'True'
    rate: '10'
    showports: 'False'
    showrf: 'False'
    type: complex
    wintype: window.WIN_BLACKMAN_hARRIS
  states:
    bus_sink: false
    bus_source: false
    bus_structure: null
    coordinate: [368, 756.0]
    rotation: 0
    state: enabled
- name: uhd_usrp_source_1_0
  id: uhd_usrp_source
  parameters:
    affinity: ''
    alias: ''
    ant0: '"RX2"'
    ant1: '"RX2"'
    ant10: '"RX2"'
    ant11: '"RX2"'
    ant12: '"RX2"'
    ant13: '"RX2"'
    ant14: '"RX2"'
    ant15: '"RX2"'
    ant16: '"RX2"'
    ant17: '"RX2"'
    ant18: '"RX2"'
    ant19: '"RX2"'
    ant2: '"RX2"'
    ant20: '"RX2"'
    ant21: '"RX2"'
    ant22: '"RX2"'
    ant23: '"RX2"'
    ant24: '"RX2"'
    ant25: '"RX2"'
    ant26: '"RX2"'
    ant27: '"RX2"'
    ant28: '"RX2"'
    ant29: '"RX2"'
    ant3: '"RX2"'
    ant30: '"RX2"'
    ant31: '"RX2"'
    ant4: '"RX2"'
    ant5: '"RX2"'
    ant6: '"RX2"'
    ant7: '"RX2"'
    ant8: '"RX2"'
    ant9: '"RX2"'
    bw0: band_width
    bw1: band_width
    bw10: '0'
    bw11: '0'
    bw12: '0'
    bw13: '0'
    bw14: '0'
    bw15: '0'
    bw16: '0'
    bw17: '0'
    bw18: '0'
    bw19: '0'
    bw2: '0'
    bw20: '0'
    bw21: '0'
    bw22: '0'
    bw23: '0'
    bw24: '0'
    bw25: '0'
    bw26: '0'
    bw27: '0'
    bw28: '0'
    bw29: '0'
    bw3: '0'
    bw30: '0'
    bw31: '0'
    bw4: '0'
    bw5: '0'
    bw6: '0'
    bw7: '0'
    bw8: '0'
    bw9: '0'
    center_freq0: freq
    center_freq1: freq
    center_freq10: '0'
    center_freq11: '0'
    center_freq12: '0'
    center_freq13: '0'
    center_freq14: '0'
    center_freq15: '0'
    center_freq16: '0'
    center_freq17: '0'
    center_freq18: '0'
    center_freq19: '0'
    center_freq2: '0'
    center_freq20: '0'
    center_freq21: '0'
    center_freq22: '0'
    center_freq23: '0'
    center_freq24: '0'
    center_freq25: '0'
    center_freq26: '0'
    center_freq27: '0'
    center_freq28: '0'
    center_freq29: '0'
    center_freq3: '0'
    center_freq30: '0'
    center_freq31: '0'
    center_freq4: '0'
    center_freq5: '0'
    center_freq6: '0'
    center_freq7: '0'
    center_freq8: '0'
    center_freq9: '0'
    clock_rate: 0e0
    clock_source0: ''
    clock_source1: ''
    clock_source2: ''
    clock_source3: ''
    clock_source4: ''
    clock_source5: ''
    clock_source6: ''
    clock_source7: ''
    comment: ''
    dc_offs0: 0+0j
    dc_offs1: 0+0j
    dc_offs10: 0+0j
    dc_offs11: 0+0j
    dc_offs12: 0+0j
    dc_offs13: 0+0j
    dc_offs14: 0+0j
    dc_offs15: 0+0j
    dc_offs16: 0+0j
    dc_offs17: 0+0j
    dc_offs18: 0+0j
    dc_offs19: 0+0j
    dc_offs2: 0+0j
    dc_offs20: 0+0j
    dc_offs21: 0+0j
    dc_offs22: 0+0j
    dc_offs23: 0+0j
    dc_offs24: 0+0j
    dc_offs25: 0+0j
    dc_offs26: 0+0j
    dc_offs27: 0+0j
    dc_offs28: 0+0j
    dc_offs29: 0+0j
    dc_offs3: 0+0j
    dc_offs30: 0+0j
    dc_offs31: 0+0j
    dc_offs4: 0+0j
    dc_offs5: 0+0j
    dc_offs6: 0+0j
    dc_offs7: 0+0j
    dc_offs8: 0+0j
    dc_offs9: 0+0j
    dc_offs_enb0: auto
    dc_offs_enb1: auto
    dc_offs_enb10: default
    dc_offs_enb11: default
    dc_offs_enb12: default
    dc_offs_enb13: default
    dc_offs_enb14: default
    dc_offs_enb15: default
    dc_offs_enb16: default
    dc_offs_enb17: default
    dc_offs_enb18: default
    dc_offs_enb19: default
    dc_offs_enb2: default
    dc_offs_enb20: default
    dc_offs_enb21: default
    dc_offs_enb22: default
    dc_offs_enb23: default
    dc_offs_enb24: default
    dc_offs_enb25: default
    dc_offs_enb26: default
    dc_offs_enb27: default
    dc_offs_enb28: default
    dc_offs_enb29: default
    dc_offs_enb3: default
    dc_offs_enb30: default
    dc_offs_enb31: default
    dc_offs_enb4: default
    dc_offs_enb5: default
    dc_offs_enb6: default
    dc_offs_enb7: default
    dc_offs_enb8: default
    dc_offs_enb9: default
    dev_addr: '"serial = 31FBCB0"'
    dev_args: ''
    gain0: '40'
    gain1: '40'
    gain10: '0'
    gain11: '0'
    gain12: '0'
    gain13: '0'
    gain14: '0'
    gain15: '0'
    gain16: '0'
    gain17: '0'
    gain18: '0'
    gain19: '0'
    gain2: '0'
    gain20: '0'
    gain21: '0'
    gain22: '0'
    gain23: '0'
    gain24: '0'
    gain25: '0'
    gain26: '0'
    gain27: '0'
    gain28: '0'
    gain29: '0'
    gain3: '0'
    gain30: '0'
    gain31: '0'
    gain4: '0'
    gain5: '0'
    gain6: '0'
    gain7: '0'
    gain8: '0'
    gain9: '0'
    gain_type0: default
    gain_type1: default
    gain_type10: default
    gain_type11: default
    gain_type12: default
    gain_type13: default
    gain_type14: default
    gain_type15: default
    gain_type16: default
    gain_type17: default
    gain_type18: default
    gain_type19: default
    gain_type2: default
    gain_type20: default
    gain_type21: default
    gain_type22: default
    gain_type23: default
    gain_type24: default
    gain_type25: default
    gain_type26: default
    gain_type27: default
    gain_type28: default
    gain_type29: default
    gain_type3: default
    gain_type30: default
    gain_type31: default
    gain_type4: default
    gain_type5: default
    gain_type6: default
    gain_type7: default
    gain_type8: default
    gain_type9: default
    iq_imbal0: 0+0j
    iq_imbal1: 0+0j
    iq_imbal10: 0+0j
    iq_imbal11: 0+0j
    iq_imbal12: 0+0j
    iq_imbal13: 0+0j
    iq_imbal14: 0+0j
    iq_imbal15: 0+0j
    iq_imbal16: 0+0j
    iq_imbal17: 0+0j
    iq_imbal18: 0+0j
    iq_imbal19: 0+0j
    iq_imbal2: 0+0j
    iq_imbal20: 0+0j
    iq_imbal21: 0+0j
    iq_imbal22: 0+0j
    iq_imbal23: 0+0j
    iq_imbal24: 0+0j
    iq_imbal25: 0+0j
    iq_imbal26: 0+0j
    iq_imbal27: 0+0j
    iq_imbal28: 0+0j
    iq_imbal29: 0+0j
    iq_imbal3: 0+0j
    iq_imbal30: 0+0j
    iq_imbal31: 0+0j
    iq_imbal4: 0+0j
    iq_imbal5: 0+0j
    iq_imbal6: 0+0j
    iq_imbal7: 0+0j
    iq_imbal8: 0+0j
    iq_imbal9: 0+0j
    iq_imbal_enb0: default
    iq_imbal_enb1: default
    iq_imbal_enb10: default
    iq_imbal_enb11: default
    iq_imbal_enb12: default
    iq_imbal_enb13: default
    iq_imbal_enb14: default
    iq_imbal_enb15: default
    iq_imbal_enb16: default
    iq_imbal_enb17: default
    iq_imbal_enb18: default
    iq_imbal_enb19: default
    iq_imbal_enb2: default
    iq_imbal_enb20: default
    iq_imbal_enb21: default
    iq_imbal_enb22: default
    iq_imbal_enb23: default
    iq_imbal_enb24: default
    iq_imbal_enb25: default
    iq_imbal_enb26: default
    iq_imbal_enb27: default
    iq_imbal_enb28: default
    iq_imbal_enb29: default
    iq_imbal_enb3: default
    iq_imbal_enb30: default
    iq_imbal_enb31: default
    iq_imbal_enb4: default
    iq_imbal_enb5: default
    iq_imbal_enb6: default
    iq_imbal_enb7: default
    iq_imbal_enb8: default
    iq_imbal_enb9: default
    lo_export0: 'False'
    lo_export1: 'False'
    lo_export10: 'False'
    lo_export11: 'False'
    lo_export12: 'False'
    lo_export13: 'False'
    lo_export14: 'False'
    lo_export15: 'False'
    lo_export16: 'False'
    lo_export17: 'False'
    lo_export18: 'False'
    lo_export19: 'False'
    lo_export2: 'False'
    lo_export20: 'False'
    lo_export21: 'False'
    lo_export22: 'False'
    lo_export23: 'False'
    lo_export24: 'False'
    lo_export25: 'False'
    lo_export26: 'False'
    lo_export27: 'False'
    lo_export28: 'False'
    lo_export29: 'False'
    lo_export3: 'False'
    lo_export30: 'False'
    lo_export31: 'False'
    lo_export4: 'False'
    lo_export5: 'False'
    lo_export6: 'False'
    lo_export7: 'False'
    lo_export8: 'False'
    lo_export9: 'False'
    lo_source0: internal
    lo_source1: internal
    lo_source10: internal
    lo_source11: internal
    lo_source12: internal
    lo_source13: internal
    lo_source14: internal
    lo_source15: internal
    lo_source16: internal
    lo_source17: internal
    lo_source18: internal
    lo_source19: internal
    lo_source2: internal
    lo_source20: internal
    lo_source21: internal
    lo_source22: internal
    lo_source23: internal
    lo_source24: internal
    lo_source25: internal
    lo_source26: internal
    lo_source27: internal
    lo_source28: internal
    lo_source29: internal
    lo_source3: internal
    lo_source30: internal
    lo_source31: internal
    lo_source4: internal
    lo_source5: internal
    lo_source6: internal
    lo_source7: internal
    lo_source8: internal
    lo_source9: internal
    maxoutbuf: '0'
    minoutbuf: '0'
    nchan: '2'
    num_mboards: '1'
    otw: ''
    rx_agc0: Default
    rx_agc1: Default
    rx_agc10: Default
    rx_agc11: Default
    rx_agc12: Default
    rx_agc13: Default
    rx_agc14: Default
    rx_agc15: Default
    rx_agc16: Default
    rx_agc17: Default
    rx_agc18: Default
    rx_agc19: Default
    rx_agc2: Default
    rx_agc20: Default
    rx_agc21: Default
    rx_agc22: Default
    rx_agc23: Default
    rx_agc24: Default
    rx_agc25: Default
    rx_agc26: Default
    rx_agc27: Default
    rx_agc28: Default
    rx_agc29: Default
    rx_agc3: Default
    rx_agc30: Default
    rx_agc31: Default
    rx_agc4: Default
    rx_agc5: Default
    rx_agc6: Default
    rx_agc7: Default
    rx_agc8: Default
    rx_agc9: Default
    samp_rate: samp_rate
    sd_spec0: A:0 B:0
    sd_spec1: ''
    sd_spec2: ''
    sd_spec3: ''
    sd_spec4: ''
    sd_spec5: ''
    sd_spec6: ''
    sd_spec7: ''
    show_lo_controls: 'False'
    start_time: '-1.0'
    stream_args: ''
    stream_chans: '[]'
    sync: pc_clock
    time_source0: ''
    time_source1: ''
    time_source2: ''
    time_source3: ''
    time_source4: ''
    time_source5: ''
    time_source6: ''
    time_source7: ''
    type: fc32
  states:
    bus_sink: false
    bus_source: false
    bus_structure: null
    coordinate: [32, 556.0]
    rotation: 0
    state: enabled
- name: uhd_usrp_source_1_0_0
  id: uhd_usrp_source
  parameters:
    affinity: ''
    alias: ''
    ant0: '"RX2"'
    ant1: '"RX2"'
    ant10: '"RX2"'
    ant11: '"RX2"'
    ant12: '"RX2"'
    ant13: '"RX2"'
    ant14: '"RX2"'
    ant15: '"RX2"'
    ant16: '"RX2"'
    ant17: '"RX2"'
    ant18: '"RX2"'
    ant19: '"RX2"'
    ant2: '"RX2"'
    ant20: '"RX2"'
    ant21: '"RX2"'
    ant22: '"RX2"'
    ant23: '"RX2"'
    ant24: '"RX2"'
    ant25: '"RX2"'
    ant26: '"RX2"'
    ant27: '"RX2"'
    ant28: '"RX2"'
    ant29: '"RX2"'
    ant3: '"RX2"'
    ant30: '"RX2"'
    ant31: '"RX2"'
    ant4: '"RX2"'
    ant5: '"RX2"'
    ant6: '"RX2"'
    ant7: '"RX2"'
    ant8: '"RX2"'
    ant9: '"RX2"'
    bw0: band_width
    bw1: band_width
    bw10: '0'
    bw11: '0'
    bw12: '0'
    bw13: '0'
    bw14: '0'
    bw15: '0'
    bw16: '0'
    bw17: '0'
    bw18: '0'
    bw19: '0'
    bw2: '0'
    bw20: '0'
    bw21: '0'
    bw22: '0'
    bw23: '0'
    bw24: '0'
    bw25: '0'
    bw26: '0'
    bw27: '0'
    bw28: '0'
    bw29: '0'
    bw3: '0'
    bw30: '0'
    bw31: '0'
    bw4: '0'
    bw5: '0'
    bw6: '0'
    bw7: '0'
    bw8: '0'
    bw9: '0'
    center_freq0: freq
    center_freq1: freq
    center_freq10: '0'
    center_freq11: '0'
    center_freq12: '0'
    center_freq13: '0'
    center_freq14: '0'
    center_freq15: '0'
    center_freq16: '0'
    center_freq17: '0'
    center_freq18: '0'
    center_freq19: '0'
    center_freq2: '0'
    center_freq20: '0'
    center_freq21: '0'
    center_freq22: '0'
    center_freq23: '0'
    center_freq24: '0'
    center_freq25: '0'
    center_freq26: '0'
    center_freq27: '0'
    center_freq28: '0'
    center_freq29: '0'
    center_freq3: '0'
    center_freq30: '0'
    center_freq31: '0'
    center_freq4: '0'
    center_freq5: '0'
    center_freq6: '0'
    center_freq7: '0'
    center_freq8: '0'
    center_freq9: '0'
    clock_rate: 0e0
    clock_source0: ''
    clock_source1: ''
    clock_source2: ''
    clock_source3: ''
    clock_source4: ''
    clock_source5: ''
    clock_source6: ''
    clock_source7: ''
    comment: ''
    dc_offs0: 0+0j
    dc_offs1: 0+0j
    dc_offs10: 0+0j
    dc_offs11: 0+0j
    dc_offs12: 0+0j
    dc_offs13: 0+0j
    dc_offs14: 0+0j
    dc_offs15: 0+0j
    dc_offs16: 0+0j
    dc_offs17: 0+0j
    dc_offs18: 0+0j
    dc_offs19: 0+0j
    dc_offs2: 0+0j
    dc_offs20: 0+0j
    dc_offs21: 0+0j
    dc_offs22: 0+0j
    dc_offs23: 0+0j
    dc_offs24: 0+0j
    dc_offs25: 0+0j
    dc_offs26: 0+0j
    dc_offs27: 0+0j
    dc_offs28: 0+0j
    dc_offs29: 0+0j
    dc_offs3: 0+0j
    dc_offs30: 0+0j
    dc_offs31: 0+0j
    dc_offs4: 0+0j
    dc_offs5: 0+0j
    dc_offs6: 0+0j
    dc_offs7: 0+0j
    dc_offs8: 0+0j
    dc_offs9: 0+0j
    dc_offs_enb0: auto
    dc_offs_enb1: auto
    dc_offs_enb10: default
    dc_offs_enb11: default
    dc_offs_enb12: default
    dc_offs_enb13: default
    dc_offs_enb14: default
    dc_offs_enb15: default
    dc_offs_enb16: default
    dc_offs_enb17: default
    dc_offs_enb18: default
    dc_offs_enb19: default
    dc_offs_enb2: default
    dc_offs_enb20: default
    dc_offs_enb21: default
    dc_offs_enb22: default
    dc_offs_enb23: default
    dc_offs_enb24: default
    dc_offs_enb25: default
    dc_offs_enb26: default
    dc_offs_enb27: default
    dc_offs_enb28: default
    dc_offs_enb29: default
    dc_offs_enb3: default
    dc_offs_enb30: default
    dc_offs_enb31: default
    dc_offs_enb4: default
    dc_offs_enb5: default
    dc_offs_enb6: default
    dc_offs_enb7: default
    dc_offs_enb8: default
    dc_offs_enb9: default
    dev_addr: '"serial = 31FBCB0"'
    dev_args: ''
    gain0: '40'
    gain1: '40'
    gain10: '0'
    gain11: '0'
    gain12: '0'
    gain13: '0'
    gain14: '0'
    gain15: '0'
    gain16: '0'
    gain17: '0'
    gain18: '0'
    gain19: '0'
    gain2: '0'
    gain20: '0'
    gain21: '0'
    gain22: '0'
    gain23: '0'
    gain24: '0'
    gain25: '0'
    gain26: '0'
    gain27: '0'
    gain28: '0'
    gain29: '0'
    gain3: '0'
    gain30: '0'
    gain31: '0'
    gain4: '0'
    gain5: '0'
    gain6: '0'
    gain7: '0'
    gain8: '0'
    gain9: '0'
    gain_type0: default
    gain_type1: default
    gain_type10: default
    gain_type11: default
    gain_type12: default
    gain_type13: default
    gain_type14: default
    gain_type15: default
    gain_type16: default
    gain_type17: default
    gain_type18: default
    gain_type19: default
    gain_type2: default
    gain_type20: default
    gain_type21: default
    gain_type22: default
    gain_type23: default
    gain_type24: default
    gain_type25: default
    gain_type26: default
    gain_type27: default
    gain_type28: default
    gain_type29: default
    gain_type3: default
    gain_type30: default
    gain_type31: default
    gain_type4: default
    gain_type5: default
    gain_type6: default
    gain_type7: default
    gain_type8: default
    gain_type9: default
    iq_imbal0: 0+0j
    iq_imbal1: 0+0j
    iq_imbal10: 0+0j
    iq_imbal11: 0+0j
    iq_imbal12: 0+0j
    iq_imbal13: 0+0j
    iq_imbal14: 0+0j
    iq_imbal15: 0+0j
    iq_imbal16: 0+0j
    iq_imbal17: 0+0j
    iq_imbal18: 0+0j
    iq_imbal19: 0+0j
    iq_imbal2: 0+0j
    iq_imbal20: 0+0j
    iq_imbal21: 0+0j
    iq_imbal22: 0+0j
    iq_imbal23: 0+0j
    iq_imbal24: 0+0j
    iq_imbal25: 0+0j
    iq_imbal26: 0+0j
    iq_imbal27: 0+0j
    iq_imbal28: 0+0j
    iq_imbal29: 0+0j
    iq_imbal3: 0+0j
    iq_imbal30: 0+0j
    iq_imbal31: 0+0j
    iq_imbal4: 0+0j
    iq_imbal5: 0+0j
    iq_imbal6: 0+0j
    iq_imbal7: 0+0j
    iq_imbal8: 0+0j
    iq_imbal9: 0+0j
    iq_imbal_enb0: default
    iq_imbal_enb1: default
    iq_imbal_enb10: default
    iq_imbal_enb11: default
    iq_imbal_enb12: default
    iq_imbal_enb13: default
    iq_imbal_enb14: default
    iq_imbal_enb15: default
    iq_imbal_enb16: default
    iq_imbal_enb17: default
    iq_imbal_enb18: default
    iq_imbal_enb19: default
    iq_imbal_enb2: default
    iq_imbal_enb20: default
    iq_imbal_enb21: default
    iq_imbal_enb22: default
    iq_imbal_enb23: default
    iq_imbal_enb24: default
    iq_imbal_enb25: default
    iq_imbal_enb26: default
    iq_imbal_enb27: default
    iq_imbal_enb28: default
    iq_imbal_enb29: default
    iq_imbal_enb3: default
    iq_imbal_enb30: default
    iq_imbal_enb31: default
    iq_imbal_enb4: default
    iq_imbal_enb5: default
    iq_imbal_enb6: default
    iq_imbal_enb7: default
    iq_imbal_enb8: default
    iq_imbal_enb9: default
    lo_export0: 'False'
    lo_export1: 'False'
    lo_export10: 'False'
    lo_export11: 'False'
    lo_export12: 'False'
    lo_export13: 'False'
    lo_export14: 'False'
    lo_export15: 'False'
    lo_export16: 'False'
    lo_export17: 'False'
    lo_export18: 'False'
    lo_export19: 'False'
    lo_export2: 'False'
    lo_export20: 'False'
    lo_export21: 'False'
    lo_export22: 'False'
    lo_export23: 'False'
    lo_export24: 'False'
    lo_export25: 'False'
    lo_export26: 'False'
    lo_export27: 'False'
    lo_export28: 'False'
    lo_export29: 'False'
    lo_export3: 'False'
    lo_export30: 'False'
    lo_export31: 'False'
    lo_export4: 'False'
    lo_export5: 'False'
    lo_export6: 'False'
    lo_export7: 'False'
    lo_export8: 'False'
    lo_export9: 'False'
    lo_source0: internal
    lo_source1: internal
    lo_source10: internal
    lo_source11: internal
    lo_source12: internal
    lo_source13: internal
    lo_source14: internal
    lo_source15: internal
    lo_source16: internal
    lo_source17: internal
    lo_source18: internal
    lo_source19: internal
    lo_source2: internal
    lo_source20: internal
    lo_source21: internal
    lo_source22: internal
    lo_source23: internal
    lo_source24: internal
    lo_source25: internal
    lo_source26: internal
    lo_source27: internal
    lo_source28: internal
    lo_source29: internal
    lo_source3: internal
    lo_source30: internal
    lo_source31: internal
    lo_source4: internal
    lo_source5: internal
    lo_source6: internal
    lo_source7: internal
    lo_source8: internal
    lo_source9: internal
    maxoutbuf: '0'
    minoutbuf: '0'
    nchan: '1'
    num_mboards: '1'
    otw: ''
    rx_agc0: Default
    rx_agc1: Default
    rx_agc10: Default
    rx_agc11: Default
    rx_agc12: Default
    rx_agc13: Default
    rx_agc14: Default
    rx_agc15: Default
    rx_agc16: Default
    rx_agc17: Default
    rx_agc18: Default
    rx_agc19: Default
    rx_agc2: Default
    rx_agc20: Default
    rx_agc21: Default
    rx_agc22: Default
    rx_agc23: Default
    rx_agc24: Default
    rx_agc25: Default
    rx_agc26: Default
    rx_agc27: Default
    rx_agc28: Default
    rx_agc29: Default
    rx_agc3: Default
    rx_agc30: Default
    rx_agc31: Default
    rx_agc4: Default
    rx_agc5: Default
    rx_agc6: Default
    rx_agc7: Default
    rx_agc8: Default
    rx_agc9: Default
    samp_rate: samp_rate
    sd_spec0: A:0
    sd_spec1: ''
    sd_spec2: ''
    sd_spec3: ''
    sd_spec4: ''
    sd_spec5: ''
    sd_spec6: ''
    sd_spec7: ''
    show_lo_controls: 'False'
    start_time: '-1.0'
    stream_args: ''
    stream_chans: '[]'
    sync: pc_clock
    time_source0: ''
    time_source1: ''
    time_source2: ''
    time_source3: ''
    time_source4: ''
    time_source5: ''
    time_source6: ''
    time_source7: ''
    type: fc32
  states:
    bus_sink: false
    bus_source: false
    bus_structure: null
    coordinate: [80, 272.0]
    rotation: 0
    state: disabled
- name: virtual_sink_0
  id: virtual_sink
  parameters:
    alias: ''
    comment: ''
    stream_id: Header Stream
  states:
    bus_sink: false
    bus_source: false
    bus_structure: null
    coordinate: [1664, 352.0]
    rotation: 0
    state: enabled
- name: virtual_sink_0_0
  id: virtual_sink
  parameters:
    alias: ''
    comment: ''
    stream_id: Header Stream2
  states:
    bus_sink: false
    bus_source: false
    bus_structure: null
    coordinate: [1352, 1248.0]
    rotation: 0
    state: enabled
- name: virtual_sink_1
  id: virtual_sink
  parameters:
    alias: ''
    comment: ''
    stream_id: Payload Stream
  states:
    bus_sink: false
    bus_source: false
    bus_structure: null
    coordinate: [1736, 384.0]
    rotation: 0
    state: enabled
- name: virtual_sink_1_0
  id: virtual_sink
  parameters:
    alias: ''
    comment: ''
    stream_id: Payload IQ
  states:
    bus_sink: false
    bus_source: false
    bus_structure: null
    coordinate: [1824, 840.0]
    rotation: 0
    state: disabled
- name: virtual_sink_1_0_0
  id: virtual_sink
  parameters:
    alias: ''
    comment: ''
    stream_id: Payload IQ2
  states:
    bus_sink: false
    bus_source: false
    bus_structure: null
    coordinate: [1320, 1816.0]
    rotation: 0
    state: disabled
- name: virtual_sink_1_1
  id: virtual_sink
  parameters:
    alias: ''
    comment: ''
    stream_id: Payload Stream2
  states:
    bus_sink: false
    bus_source: false
    bus_structure: null
    coordinate: [1456, 1280.0]
    rotation: 0
    state: enabled
- name: virtual_source_0
  id: virtual_source
  parameters:
    alias: ''
    comment: ''
    stream_id: Header Stream
  states:
    bus_sink: false
    bus_source: false
    bus_structure: null
    coordinate: [592, 632.0]
    rotation: 0
    state: enabled
- name: virtual_source_0_0
  id: virtual_source
  parameters:
    alias: ''
    comment: ''
    stream_id: Payload IQ
  states:
    bus_sink: false
    bus_source: false
    bus_structure: null
    coordinate: [624, 992.0]
    rotation: 0
    state: disabled
- name: virtual_source_0_0_0
  id: virtual_source
  parameters:
    alias: ''
    comment: ''
    stream_id: Payload IQ2
  states:
    bus_sink: false
    bus_source: false
    bus_structure: null
    coordinate: [24, 1968.0]
    rotation: 0
    state: disabled
- name: virtual_source_0_1
  id: virtual_source
  parameters:
    alias: ''
    comment: ''
    stream_id: Header Stream2
  states:
    bus_sink: false
    bus_source: false
    bus_structure: null
    coordinate: [32, 1584.0]
    rotation: 0
    state: enabled
- name: virtual_source_1
  id: virtual_source
  parameters:
    alias: ''
    comment: "\u4E0D\u542BCP"
    stream_id: Payload Stream
  states:
    bus_sink: false
    bus_source: false
    bus_structure: null
    coordinate: [592, 840.0]
    rotation: 0
    state: enabled
- name: virtual_source_1_0
  id: virtual_source
  parameters:
    alias: ''
    comment: "\u4E0D\u542BCP"
    stream_id: Payload Stream2
  states:
    bus_sink: false
    bus_source: false
    bus_structure: null
    coordinate: [8, 1816.0]
    rotation: 0
    state: enabled

connections:
- [analog_frequency_modulator_fc_0, '0', blocks_multiply_xx_0, '0']
- [analog_frequency_modulator_fc_0_0, '0', blocks_multiply_xx_0_0, '0']
- [blocks_delay_0, '0', blocks_multiply_xx_0, '1']
- [blocks_delay_0_0, '0', blocks_multiply_xx_0_0, '1']
- [blocks_multiply_xx_0, '0', blocks_file_sink_0, '0']
- [blocks_multiply_xx_0, '0', digital_header_payload_demux_0, '0']
- [blocks_multiply_xx_0_0, '0', blocks_file_sink_0_0, '0']
- [blocks_multiply_xx_0_0, '0', digital_header_payload_demux_0_0, '0']
- [blocks_repack_bits_bb_0, '0', digital_crc32_bb_0, '0']
- [blocks_repack_bits_bb_0_0, '0', digital_crc32_bb_0_0, '0']
- [blocks_throttle_0, '0', blocks_delay_0, '0']
- [blocks_throttle_0, '0', digital_ofdm_sync_sc_cfb_0, '0']
- [blocks_throttle_1, '0', blocks_delay_0_0, '0']
- [blocks_throttle_1, '0', digital_ofdm_sync_sc_cfb_0_0, '0']
- [digital_constellation_decoder_cb_0, '0', digital_packet_headerparser_b_0, '0']
- [digital_constellation_decoder_cb_0_0, '0', digital_packet_headerparser_b_0_0, '0']
- [digital_constellation_decoder_cb_1, '0', blocks_repack_bits_bb_0, '0']
- [digital_constellation_decoder_cb_1_0, '0', blocks_repack_bits_bb_0_0, '0']
- [digital_crc32_bb_0, '0', blocks_file_sink_14, '0']
- [digital_crc32_bb_0_0, '0', blocks_file_sink_14_0, '0']
- [digital_header_payload_demux_0, '0', virtual_sink_0, '0']
- [digital_header_payload_demux_0, '1', virtual_sink_1, '0']
- [digital_header_payload_demux_0_0, '0', virtual_sink_0_0, '0']
- [digital_header_payload_demux_0_0, '1', virtual_sink_1_1, '0']
- [digital_ofdm_chanest_vcvc_0, '0', digital_ofdm_frame_equalizer_vcvc_0, '0']
- [digital_ofdm_chanest_vcvc_0_0, '0', digital_ofdm_frame_equalizer_vcvc_0_0, '0']
- [digital_ofdm_frame_equalizer_vcvc_0, '0', digital_ofdm_serializer_vcc_header, '0']
- [digital_ofdm_frame_equalizer_vcvc_0_0, '0', digital_ofdm_serializer_vcc_header_0,
  '0']
- [digital_ofdm_frame_equalizer_vcvc_1, '0', digital_ofdm_serializer_vcc_payload,
  '0']
- [digital_ofdm_frame_equalizer_vcvc_1_0, '0', digital_ofdm_serializer_vcc_payload_0,
  '0']
- [digital_ofdm_serializer_vcc_header, '0', digital_constellation_decoder_cb_0, '0']
- [digital_ofdm_serializer_vcc_header_0, '0', digital_constellation_decoder_cb_0_0,
  '0']
- [digital_ofdm_serializer_vcc_payload, '0', virtual_sink_1_0, '0']
- [digital_ofdm_serializer_vcc_payload_0, '0', virtual_sink_1_0_0, '0']
- [digital_ofdm_sync_sc_cfb_0, '0', analog_frequency_modulator_fc_0, '0']
- [digital_ofdm_sync_sc_cfb_0, '0', blocks_file_sink_1, '0']
- [digital_ofdm_sync_sc_cfb_0, '1', blocks_file_sink_1_1, '0']
- [digital_ofdm_sync_sc_cfb_0, '1', digital_header_payload_demux_0, '1']
- [digital_ofdm_sync_sc_cfb_0_0, '0', analog_frequency_modulator_fc_0_0, '0']
- [digital_ofdm_sync_sc_cfb_0_0, '1', digital_header_payload_demux_0_0, '1']
- [digital_packet_headerparser_b_0, header_data, digital_header_payload_demux_0, header_data]
- [digital_packet_headerparser_b_0_0, header_data, digital_header_payload_demux_0_0,
  header_data]
- [fft_vxx_0, '0', digital_ofdm_chanest_vcvc_0, '0']
- [fft_vxx_0_0, '0', digital_ofdm_chanest_vcvc_0_0, '0']
- [fft_vxx_1, '0', digital_ofdm_frame_equalizer_vcvc_1, '0']
- [fft_vxx_1_0, '0', digital_ofdm_frame_equalizer_vcvc_1_0, '0']
- [network_tcp_source_0, '0', blocks_delay_0, '0']
- [network_tcp_source_0, '0', blocks_file_sink_1_0_0, '0']
- [network_tcp_source_0, '0', digital_ofdm_sync_sc_cfb_0, '0']
- [network_tcp_source_0, '0', qtgui_sink_x_0_0, '0']
- [uhd_usrp_source_1_0, '0', blocks_delay_0, '0']
- [uhd_usrp_source_1_0, '0', blocks_file_sink_1_0_0, '0']
- [uhd_usrp_source_1_0, '0', blocks_throttle_0, '0']
- [uhd_usrp_source_1_0, '0', digital_ofdm_sync_sc_cfb_0, '0']
- [uhd_usrp_source_1_0, '0', qtgui_sink_x_0_0, '0']
- [uhd_usrp_source_1_0, '1', blocks_delay_0_0, '0']
- [uhd_usrp_source_1_0, '1', blocks_file_sink_1_0, '0']
- [uhd_usrp_source_1_0, '1', blocks_throttle_1, '0']
- [uhd_usrp_source_1_0, '1', digital_ofdm_sync_sc_cfb_0_0, '0']
- [uhd_usrp_source_1_0, '1', qtgui_sink_x_0_1, '0']
- [uhd_usrp_source_1_0_0, '0', blocks_delay_0, '0']
- [uhd_usrp_source_1_0_0, '0', blocks_file_sink_1_0_0, '0']
- [uhd_usrp_source_1_0_0, '0', digital_ofdm_sync_sc_cfb_0, '0']
- [uhd_usrp_source_1_0_0, '0', qtgui_sink_x_0_0, '0']
- [virtual_source_0, '0', blocks_file_sink_9, '0']
- [virtual_source_0, '0', fft_vxx_0, '0']
- [virtual_source_0_0, '0', digital_constellation_decoder_cb_1, '0']
- [virtual_source_0_0_0, '0', digital_constellation_decoder_cb_1_0, '0']
- [virtual_source_0_1, '0', blocks_file_sink_9_0, '0']
- [virtual_source_0_1, '0', fft_vxx_0_0, '0']
- [virtual_source_1, '0', blocks_file_sink_8, '0']
- [virtual_source_1, '0', fft_vxx_1, '0']
- [virtual_source_1_0, '0', blocks_file_sink_8_0, '0']
- [virtual_source_1_0, '0', fft_vxx_1_0, '0']

metadata:
  file_format: 1
