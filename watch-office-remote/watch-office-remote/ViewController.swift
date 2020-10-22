//
//  ViewController.swift
//  watch-office-remote
//
//  Created by Daniel Gruen on 10/15/20.
//

import UIKit

class ViewController: UIViewController, UIPickerViewDelegate, UIPickerViewDataSource  {
    
    var seasons: [Int] = [1]
    var episodes: [Int] = [1, 2, 3, 4, 5, 6]
    
    var selectedSeason: Int = 1
    var selectedEpisode: Int = 1

    override func viewDidLoad() {
        super.viewDidLoad()
        
        // Connect data:
        self.seasonPicker.delegate = self
        self.seasonPicker.dataSource = seasons as? UIPickerViewDataSource
        
        self.episodePicker.delegate = self
        self.episodePicker.dataSource = episodes as? UIPickerViewDataSource
    }
    
    func numberOfComponents(in pickerView: UIPickerView) -> Int {
        return 1
    }
    
    func pickerView(_ pickerView: UIPickerView, numberOfRowsInComponent component: Int) -> Int {
        if pickerView == seasonPicker {
            return seasons.count
        } else if pickerView == episodePicker {
            return episodes.count
        } else {
            return 1
        }
    }
    
    // The data to return for the row and component (column) that's being passed in
    func pickerView(_ pickerView: UIPickerView, titleForRow row: Int, forComponent component: Int) -> String? {
        if pickerView == seasonPicker {
            return String(seasons[row])
        } else if pickerView == episodePicker {
            return String(episodes[row])
        } else {
            return "Error"
        }
    }
    
    func pickerView(_ pickerView: UIPickerView, didSelectRow row: Int, inComponent component: Int) {
        if pickerView == seasonPicker {
            selectedSeason = seasons[row]
        } else if pickerView == episodePicker {
            selectedEpisode = episodes[row]
        }
        print(selectedSeason, selectedEpisode)
    }

    @IBAction func TvOffButtonPushed(_ sender: UIButton) {
        let url = URL(string: "http://192.168.0.134:5000/tv-power?status=off")!

        let task = URLSession.shared.dataTask(with: url) {(data, response, error) in
            guard let data = data else { return }
            print(String(data: data, encoding: .utf8)!)
        }

        task.resume()
        
    }
    
    @IBAction func TvOnButtonPushed(_ sender: UIButton) {
        let url = URL(string: "http://192.168.0.134:5000/tv-power?status=on")!

        let task = URLSession.shared.dataTask(with: url) {(data, response, error) in
            guard let data = data else { return }
            print(String(data: data, encoding: .utf8)!)
        }

        task.resume()
    }
    
    @IBOutlet weak var seasonPicker: UIPickerView!
        
    
    @IBOutlet weak var episodePicker: UIPickerView!
    
    @IBAction func startSelectedEpisodeClicked(_ sender: UIButton) {
        let url = URL(string: "http://192.168.0.134:5000/select?season=\(selectedSeason)&episode=\(selectedEpisode)")!

        let task = URLSession.shared.dataTask(with: url) {(data, response, error) in
            guard let data = data else { return }
            print(String(data: data, encoding: .utf8)!)
        }

        task.resume()
    }
    
    
    @IBAction func pauseButtonPressed(_ sender: UIButton) {
        let url = URL(string: "http://192.168.0.134:5000/pause")!

        let task = URLSession.shared.dataTask(with: url) {(data, response, error) in
            guard let data = data else { return }
            print(String(data: data, encoding: .utf8)!)
        }

        task.resume()
    }
    
    @IBAction func resumeButtonPressed(_ sender: UIButton) {
        let url = URL(string: "http://192.168.0.134:5000/play")!

        let task = URLSession.shared.dataTask(with: url) {(data, response, error) in
            guard let data = data else { return }
            print(String(data: data, encoding: .utf8)!)
        }

        task.resume()
    }
    
}

