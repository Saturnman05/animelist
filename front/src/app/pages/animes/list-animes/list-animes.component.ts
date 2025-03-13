import { Component } from '@angular/core';

import { Anime } from '../../../models/anime.model';
import { NavBarComponent } from '../../../components/nav-bar/nav-bar.component';
import { AnimeGridComponent } from '../../../components/anime-grid/anime-grid.component';

@Component({
  selector: 'app-list-animes',
  imports: [AnimeGridComponent, NavBarComponent],
  templateUrl: './list-animes.component.html',
  styleUrl: './list-animes.component.css',
})
export class ListAnimesComponent {
  animes: Anime[] = [
    {
      id: '1',
      title:
        'Shingeki no Kyojin fsadf fasdfdsa asdfsadf sadfasdf sadfsdaf dsafasdf',
      genre: 'Action',
      author: 'Hisayama',
      amountEpisodes: 12,
      image:
        'https://th.bing.com/th/id/OIP.-H-kZ8eWI-WdPoulO34xnAHaKe?rs=1&pid=ImgDetMain',
    },
    {
      id: '2',
      title: 'Death Note',
      genre: 'Mistery',
      author: 'Tsugumi Oba & Takeshi Obata',
      amountEpisodes: 12,
      image:
        'https://m.media-amazon.com/images/M/MV5BNjRiNmNjMmMtN2U2Yi00ODgxLTk3OTMtMmI1MTI1NjYyZTEzXkEyXkFqcGdeQXVyNjAwNDUxODI@._V1_.jpg',
    },
    {
      id: '3',
      title: 'Jujutsu Kaisen',
      genre: 'Action',
      author: 'Gege Akutami',
      amountEpisodes: 12,
      image:
        'https://th.bing.com/th/id/OIP.76NLv1fDo2vao1OUjeyEzgHaKf?rs=1&pid=ImgDetMain',
    },
  ];
}
