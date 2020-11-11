import { Component, OnInit, Input } from '@angular/core';
import { PresencaModel } from '../Presenca-model';

@Component({
  selector: 'app-Presenca-item',
  templateUrl: './Presenca-item.component.html',
  styleUrls: ['./Presenca-item.component.css']
})
export class PresencaItemComponent implements OnInit {

  @Input() Presenca: PresencaModel

  constructor() { }

  ngOnInit() {
  }

}
