import { v4 as uuid } from 'uuid';

export const products = [
  {
    id: uuid(),
    createdAt: '27/10/2022',
    description: 'The IWA World Water Congress & Exhibition is the global event for water professionals covering the full water cycle. Join over 10,000 leading water professionals and companies convened by the International Water Association.',
    media: '/static/images/products/event1.png',
    title: 'IWA World Water Congress & Exhibition',
    totalDownloads: '594'
  },
  {
    id: uuid(),
    createdAt: '21/011/2022',
    description: 'The first edition of the IWA Digital Water Summit will take place under the tagline “Join the transformation journey” designed to be the reference in digitalisation for the global water sector.',
    media: '/static/images/products/event2.png',
    title: 'Digital Water Summit',
    totalDownloads: '625'
  },
  {
    id: uuid(),
    createdAt: '25/01/2023',
    description: 'The central theme of the conference is ‘Water Reuse: Overcoming Challenges of Growth and Climate Change’. This thematic framework shall help moving forward to create sustainable water reuse solutions by a multidisciplinary cooperation',
    media: '/static/images/products/event3.png',
    title: '13th IWA International Conference On Water Reclamation',
    totalDownloads: '857'
  },
  {
    id: uuid(),
    createdAt: '10/02/2023',
    description: 'The IWA Biofilms 2022 conference venue is the beautiful island of Phuket within the city of Patong. This convenient location offers a diversity of lodging options at various price points.',
    media: '/static/images/products/event4.png',
    title: 'IWA Biofilms 2023 Conference',
    totalDownloads: '406'
  },
  {
    id: uuid(),
    createdAt: '20/03/2023',
    description: 'WaterCampus Leeuwarden is hosting the second edition of the European Water Technology Week.',
    media: '/static/images/products/event5.png',
    title: 'European Water Technology Week 2023',
    totalDownloads: '857'
  },
  {
    id: uuid(),
    createdAt: '10/05/2023',
    description: 'Wetlands International Europe, EuroNatur, GEOTA, RiverWatch and WWF Adria invite you to the third European Rivers Summit (ERS) in Brussels, Belgium',
    media: '/static/images/products/event6.png',
    title: 'European Rivers Summit 2022',
    totalDownloads: '406'
  }
  
];
