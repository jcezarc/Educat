import { Component, OnInit, Input } from '@angular/core';
import { AulaModel } from '../Aula-model';

@Component({
  selector: 'app-Aula-item',
  templateUrl: './Aula-item.component.html',
  styleUrls: ['./Aula-item.component.css']
})
export class AulaItemComponent implements OnInit {

  @Input() Aula: AulaModel

  constructor() { }

  ngOnInit() {
  }

}
