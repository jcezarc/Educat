import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';

@Component({
  selector: 'app-check-button',
  templateUrl: './check-button.component.html',
  styleUrls: ['./check-button.component.css']
})
export class CheckButtonComponent implements OnInit {

  @Output() check = new EventEmitter()


  constructor() { }

  ngOnInit() {
  }

  emitEventDelete(){
    this.check.emit()
  }

}
