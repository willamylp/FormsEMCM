
let chartConfig = {
  type: 'hbar',
  fontFamily: 'Arial',
  title: {
    text: 'Status de Verificação dos Hosts',
    backgroundColor: 'none',
    fontColor: '#666666',
    fontFamily: 'Arial',
    fontSize: '18px'
  },
  plot: {
    animation: {
      delay: 300,
      effect: 'ANIMATION_EXPAND_TOP',
      method: 'ANIMATION_LINEAR',
      sequence: 'ANIMATION_BY_PLOT_AND_NODE',
      speed: '250'
    },
    barsOverlap: '100%',
    borderRadius: '8px',
    hoverState: {
      visible: false
    }
  },
  plotarea: {
    margin: '60px 20px 20px 140px'
  },
  scaleX: {
    values: ['10.143.4.50/81', '10.143.7.37/80', 'servidor/80', '192.168.1.4/80', '8.8.8.8/80'],
    guide: {
      visible: false
    },
    item: {
      paddingRight: '20px',
      autoAlign: true,
      fontSize: '14px',
      rules: [
        {
          fontColor: '#FA8452',
          rule: '%i==0'
        },
        {
          fontColor: '#FCAE48',
          rule: '%i==1'
        },
        {
          fontColor: '#FCCC65',
          rule: '%i==2'
        },
        {
          fontColor: '#A0BE4A',
          rule: '%i==3'
        },
        {
          fontColor: '#6FA6DF',
          rule: '%i==4'
        }
      ]
    },
    lineColor: 'none',
    tick: {
      visible: false
    }
  },
  scaleY: {
    guide: {
      visible: false
    },
    visible: false
  },
  
  labels: [
    {
      text: 'PING',
      fontColor: '#111111',
      fontSize: '14px',
      x: '15%',
      y: '10%'
    },
    {
      text: 'HOSTS/PORTA',
      fontColor: '#111111',
      fontSize: '14px',
      x: '1%',
      y: '10%'
    }
  ],
 
  
  series: [
    {
      values: [100, 100, 100, 100, 100],
      tooltip: {
        visible: false
      },
      backgroundColor: '#f2f2f2',
      barWidth: '40px',
      borderColor: '#e8e3e3',
      borderWidth: '2px',
      fillAngle: 90
    },
    {
      values: [1, 12, 5, 10, 7],
      valueBox: {
        text: '%v',
        alpha: 0.6,
        decimals: 0,
        fontColor: '#A4A4A4',
        fontSize: '14px',
        placement: 'top-out'
      },
      barWidth: '32px',
      maxTrackers: 0,
      rules: [
        {
          backgroundColor: '#FA8452',
          rule: '%i==0'
        },
        {
          backgroundColor: '#FCAE48',
          rule: '%i==1'
        },
        {
          backgroundColor: '#FCCC65',
          rule: '%i==2'
        },
        {
          backgroundColor: '#A0BE4A',
          rule: '%i==3'
        },
        {
          backgroundColor: '#6FA6DF',
          rule: '%i==4'
        }
      ]
    }
  ]
};
 
