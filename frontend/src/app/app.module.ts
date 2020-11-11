import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpModule } from '@angular/http';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { RouterModule } from '@angular/router';
import { AppComponent } from './app.component';
import { ROUTES } from './app.routes';
import { AlunoComponent } from './Aluno/Aluno-component';
import { AlunoItemComponent } from './Aluno/Aluno-item/Aluno-item.component';
import { AlunoService } from './Aluno/Aluno-service';
import { AlunoListComponent } from './Aluno/Aluno-list/Aluno-list.component';
import { NewAlunoComponent } from './Aluno/new-Aluno/new-Aluno.component';
import { ProfessorComponent } from './Professor/Professor-component';
import { ProfessorItemComponent } from './Professor/Professor-item/Professor-item.component';
import { ProfessorService } from './Professor/Professor-service';
import { ProfessorListComponent } from './Professor/Professor-list/Professor-list.component';
import { NewProfessorComponent } from './Professor/new-Professor/new-Professor.component';
import { AulaComponent } from './Aula/Aula-component';
import { AulaItemComponent } from './Aula/Aula-item/Aula-item.component';
import { AulaService } from './Aula/Aula-service';
import { AulaListComponent } from './Aula/Aula-list/Aula-list.component';
import { NewAulaComponent } from './Aula/new-Aula/new-Aula.component';
import { PresencaComponent } from './Presenca/Presenca-component';
import { PresencaItemComponent } from './Presenca/Presenca-item/Presenca-item.component';
import { PresencaService } from './Presenca/Presenca-service';
import { PresencaListComponent } from './Presenca/Presenca-list/Presenca-list.component';
import { NewPresencaComponent } from './Presenca/new-Presenca/new-Presenca.component';

import { NavigatorComponent } from './shared/navigator/navigator.component';
import { SearchBarComponent } from './shared/search-bar/search-bar.component';
import { DeleteButtonComponent } from './shared/delete-button/delete-button.component';
import { AuthService } from './shared/auth-service'
import { HeaderComponent } from './header/header.component'

@NgModule({
  declarations: [
    AppComponent,
    AlunoComponent,
    AlunoItemComponent,
    AlunoListComponent,
    NewAlunoComponent,
    ProfessorComponent,
    ProfessorItemComponent,
    ProfessorListComponent,
    NewProfessorComponent,
    AulaComponent,
    AulaItemComponent,
    AulaListComponent,
    NewAulaComponent,
    PresencaComponent,
    PresencaItemComponent,
    PresencaListComponent,
    NewPresencaComponent,

    HeaderComponent,
    SearchBarComponent,
    NavigatorComponent,
    DeleteButtonComponent
  ],
  imports: [
    BrowserModule,
    HttpModule,
    FormsModule, ReactiveFormsModule,
    RouterModule.forRoot(ROUTES)
  ],
  providers: [
    AuthService,
AlunoService,
ProfessorService,
AulaService,
PresencaService,

  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
