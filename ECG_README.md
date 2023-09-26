# ECG_README.md

#### Description
These data were extracted from the European ST-T database from [physionet](https://physionet.org/about/database/). A full description can be found at https://physionet.org/content/edb/1.0.0/. Excerpts of this description are included below.

The European ST-T Database is intended to be used for evaluation of algorithms for analysis of ST and T-wave changes. This database consists of 90 annotated excerpts of ambulatory ECG recordings from 79 subjects. The subjects were 70 men aged 30 to 84, and 8 women aged 55 to 71. Myocardial ischemia was diagnosed or suspected for each subject.

Two cardiologists worked independently to annotate each record beat-by-beat and for changes in ST segment and T-wave morphology, rhythm, and signal quality. A description of the annotation categories can be seen in the table below.


#### Structure
Data from a single subject were placed into a more easily accessible format on 7/26/22 by DJ.
This simplified data file contains the following fields:
- ecg_voltage: an array of electrocardiogram data
- fs: the sampling frequency in Hz
- label_samples: the samples when an event occurred
- label_symbols: the corresponding symbols (representing an event type as - described in the table below)
- subject_id: an identifier for the subject
- electrode: the name of the ECG electrode being recorded
- units: the voltage units of ecg_voltage


|index | symbol|     code |                                   description
|------|-------|----------|----------------------------------------------
| 0    |       |   NOTANN |                      Not an actual annotation
| 1    |   N   |   NORMAL |                                   Normal beat
| 2    |   L   |     LBBB |                 Left bundle branch block beat
| 3    |   R   |     RBBB |                Right bundle branch block beat
| 4    |   a   |    ABERR |               Aberrated atrial premature beat
| 5    |   V   |      PVC |             Premature ventricular contraction
| 6    |   F   |   FUSION |         Fusion of ventricular and normal beat
| 7    |   J   |      NPC |             Nodal (junctional) premature beat
| 8    |   A   |      APC |                  Atrial premature contraction
| 9    |   S   |     SVPB |    Premature or ectopic supraventricular beat
|10    |   E   |     VESC |                       Ventricular escape beat
|11    |   j   |     NESC |                Nodal (junctional) escape beat
|12    |   /   |     PACE |                                    Paced beat
|13    |   Q   |  UNKNOWN |                           Unclassifiable beat
|14    |   ~   |    NOISE |                         Signal quality change
|16    |   |   |    ARFCT |                    Isolated QRS-like artifact
|18    |   s   |     STCH |                                     ST change
|19    |   T   |      TCH |                                 T-wave change
|20    |   *   |  SYSTOLE |                                       Systole
|21    |   D   | DIASTOLE |                                      Diastole
|22    |   "   |     NOTE |                            Comment annotation
|23    |   =   |  MEASURE |                        Measurement annotation
|24    |   p   |    PWAVE |                                   P-wave peak
|25    |   B   |      BBB |             Left or right bundle branch block
|26    |   ^   |   PACESP |                     Non-conducted pacer spike
|27    |   t   |    TWAVE |                                   T-wave peak
|28    |   +   |   RHYTHM |                                 Rhythm change
|29    |   u   |    UWAVE |                                   U-wave peak
|30    |   ?   |    LEARN |                                      Learning
|31    |   !   |    FLWAV |                      Ventricular flutter wave
|32    |   [   |     VFON |     Start of ventricular flutter/fibrillation
|33    |   ]   |    VFOFF |       End of ventricular flutter/fibrillation
|34    |   e   |     AESC |                            Atrial escape beat
|35    |   n   |    SVESC |                  Supraventricular escape beat
|36    |   @   |     LINK | Link to external data (aux_note contains URL)
|37    |   x   |     NAPC |            Non-conducted P-wave (blocked APB)
|38    |   f   |     PFUS |               Fusion of paced and normal beat
|39    |   (   |     WFON |                                Waveform onset
|40    |   )   |    WFOFF |                                  Waveform end
|41    |   r   |     RONT |      R-on-T premature ventricular contraction


#### References
When using this resource, please cite the original publication:

Taddei A, Distante G, Emdin M, Pisani P, Moody GB, Zeelenberg C, Marchesi C. The European ST-T Database: standard for evaluating systems for the analysis of ST-T changes in ambulatory electrocardiography. European Heart Journal 13: 1164-1172 (1992).

Please include the standard citation for PhysioNet:


Goldberger, A., Amaral, L., Glass, L., Hausdorff, J., Ivanov, P. C., Mark, R., ... & Stanley, H. E. (2000). PhysioBank, PhysioToolkit, and PhysioNet: Components of a new research resource for complex physiologic signals. Circulation [Online]. 101 (23), pp. e215–e220.
