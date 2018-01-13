from TCLCPhase1.AnalysisLib.process_file.process_malaysia_kini_data import process_malaysia_kini_data


def test1():
    result = process_malaysia_kini_data('./sample_data/malaysia_kini')
    expected = [['Shell to offer reimbursement after accidentally doubling fuel prices '
                 'https://t.co/MVbDU03vzq https://t.co/pcVhkEVB6E',
                 '18',
                 '05',
                 '17']]
    assert result == expected
