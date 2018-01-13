from TCLCPhase1.AnalysisLib.process_file.process_lowyat_data import process_lowyat_data


def test1():
    result = process_lowyat_data('./sample_data/lowyat')
    expected = [
        ['PRU14 inkambing!', '08', '06', '17'], # 08 June 2017
        ['>senyum tersengih sengih tuNearlee', '08', '06', '17'],
        ['bangga-nya', '08', '06', '17'],
        ['gloves mj', '08', '06', '17'],
        ['Comel', '08', '06', '17'],
        ['behind bars?', '08', '06', '17'],
        ['installing window panes?', '08', '06', '17']
    ]
    assert result == expected
