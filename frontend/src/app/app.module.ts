import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpModule } from '@angular/http';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { RouterModule } from '@angular/router';
import { AppComponent } from './app.component';
import { ROUTES } from './app.routes';
import { AulaComponent } from './Aula/Aula-component';
import { AulaItemComponent } from './Aula/Aula-item/Aula-item.component';
import { AulaService } from './Aula/Aula-service';
import { AulaListComponent } from './Aula/Aula-list/Aula-list.component';

import { NavigatorComponent } from './shared/navigator/navigator.component';
import { SearchBarComponent } from './shared/search-bar/search-bar.component';
import { HeaderComponent } from './header/header.component'

@NgModule({
  declarations: [
    AppComponent,
    AulaComponent,
    AulaItemComponent,
    AulaListComponent,

    HeaderComponent,
    SearchBarComponent,
    NavigatorComponent,
  ],
  imports: [
    BrowserModule,
    HttpModule,
    FormsModule, ReactiveFormsModule,
    RouterModule.forRoot(ROUTES)
  ],
  providers: [
    AulaService,
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
